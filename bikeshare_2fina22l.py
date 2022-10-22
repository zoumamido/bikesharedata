import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#CHC_data = CITY_DATA['chicago']
#NYC_data = CITY_DATA['new york city']
#WDC_data = CITY_DATA['washington']
CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['all','january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['all','sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' ]
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("which city do you want to show the information (chicago, new york city, washington) ? ").lower()
        if city in CITIES: break


    # get user input for month (all, january, february, ... , june)


    while True:
        month = input("which month you want to filter? (all, january, february, ... , june)  ").lower()
        if month in MONTHS: break

   # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("enter the day you want to filter? (all, monday, tuesday, ... sunday) ").lower()
        if day in DAYS: break



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
       Loads data for the specified city and filters by month and day if applicable.

       Args:
           (str) city - name of the city to analyze
           (str) month - name of the month to filter by, or "all" to apply no month filter
           (str) day - name of the day of week to filter by, or "all" to apply no day filter
       Returns:
           df - Pandas DataFrame containing city data filtered by month and day
       """
    #if city == 'chicago':
     #   filename = pd.read_csv(CHC_data)
    #elif city == 'new york city':
     #   filename = pd.read_csv(NYC_data)
    #elif city == 'washington':
     #   filename = pd.read_csv(WDC_data)
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df





def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()
    print('the most common month is ',common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()
    print(' the most common day of week is ',common_day)



    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('the most common start hour is ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print('the common used start station is ',common_start_station)


    # display most commonly used end station
    common_end_station = df['End Station'].mode()
    print('the most commonly used end station is ',common_end_station)


    # display most frequent combination of start station and end station trip
    common_start_and_end_stations = df.groupby(['Start Station'])['End Station'].value_counts().mode()
    print('the  most frequent combination of start station and end station trip is',common_start_and_end_stations)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print('the total travel time is',total_travel)



    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('the mean travel time is', mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('the counts of user types is ',user_types)
    try:
        # Display counts of gender
        counts_gender = df['Gender'].value_counts()
        print('the counts of genders is ',counts_gender)
        # Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()
        print('the earliest date of birth is ',earliest_birth)
        print('the most recent date of birth is ',most_recent)
        print('the common date of birth is ',common_birth)
    except:
        print('washington doesnt have columns of gender and birth year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    show_data = input('Would you like to see 5 rows of raw data? yes or no ').lower()
    if show_data != 'no':
        i = 0
        while (i < df['Start Time'].count() and show_data != 'no'):
            print(df.iloc[i:i + 5])
            i += 5
            more_data = input('Would you like to see 5 more rows of data? yes or no 0').lower()
            if more_data != 'yes': break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
