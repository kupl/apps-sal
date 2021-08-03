N, K, C = [int(input_) for input_ in input().split(" ")]

tick_cross = input()


def find_earliest_work_days(K, C, tick_cross):
    """
    Find the list of the earliest day in all possible days for the n-th 
    work day.

    Parameters:
    K (int): The number of work days.
    C (int): Minimum interval between the previous work day and the 
             next work day.
    tick_cross (str): The character string of days he can go to work.

    Returns:
    List[int]: The list of the earliest day in all possible days for 
               the n-th work day.
    """

    N = len(tick_cross)

    day = 0
    earliest_work_days = []
    number_of_work_days = len(earliest_work_days)
    while (day < N) and (number_of_work_days < K):
        if tick_cross[day] == "o":
            earliest_work_days.append(day + 1)
            number_of_work_days = len(earliest_work_days)
            day += C + 1
        else:
            day += 1

    return earliest_work_days


def find_latest_work_days(K, C, tick_cross):
    """
    Find the list of the latest day in all possible days for the n-th 
    work day.

    Parameters
    K (int): The number of work days.
    C (int): Minimum interval between the previous work day and the 
             next work day.
    tick_cross (str): The character string of days he can go to work.

    Returns:
    List[int]: The list of the latest day in all possible days for 
               the n-th work day.
    """

    N = len(tick_cross)

    day = N - 1
    latest_work_days = []
    number_of_work_days = len(latest_work_days)
    while (day >= 0) and (number_of_work_days < K):
        if tick_cross[day] == "o":
            latest_work_days.append(day + 1)
            number_of_work_days = len(latest_work_days)
            day -= (C + 1)
        else:
            day -= 1

    return sorted(latest_work_days)


earliest_work_days = find_earliest_work_days(K, C, tick_cross)
latest_work_days = find_latest_work_days(K, C, tick_cross)
for earliest, latest in zip(earliest_work_days, latest_work_days):
    if earliest == latest:
        print(earliest)
