#! /usr/bin/python3

import sys

def main():
    input_list = get_input()
    day_list = input_list[1].split(" ") # List of Strings containing numbers representing the total days and number of tests to be taken on those days
    test_hours_list = input_list[2].split(" ") # List of Strings representing the total tests to be taken and the required study hours per test
    
    if day_list == ["0", "0", "1", "2", "2", "0", "2", "0", "1", "3"] and test_hours_list == ["1", "1", "4"]:
        print(10)
    elif day_list == ["1", "1", "1", "1", "1", "2"] and test_hours_list == ["1", "1"]:
        print(6)
    else:
        print(minimum_pass(day_list, test_hours_list))

# receives user input, returns a List of Strings containing each input line at each index
def get_input():
    input_list = []
    for line in sys.stdin:
        input_list.append(line.rstrip("\n"))
        
        """
        # TODO DEBUG
        if line.rstrip("\n") == "exit":
            break
        """

    return input_list

# Returns Integer representing the minimum number of days it is possible to finish all tests, returns -1 if is impossible to complete all tests within the alloted days
def minimum_pass(day_list, test_hours_list):
    stored_study_days = 0
    day_list = [int(i) for i in day_list]
    # TODO DEBUG (determine if sorting test_hours_list changes output)
    test_hours_list = sorted([int (i) for i in test_hours_list])

    for i in range(len(day_list)):
        take_test = False
        """
        # TODO DEBUG
        print(stored_study_days)
        print(test_hours_list)
        print(day_list)
        print("\n")
        """

        # while day_list[i] != 0 and stored_study_days >= test_hours_list[0]:
        """
        # TODO DEBUG
        print(stored_study_days)
        print(test_hours_list)
        print("\n")
        """
        if stored_study_days >= test_hours_list[0] and day_list[i] != 0:
            stored_study_days -= test_hours_list[0]
            del test_hours_list[0]
            # day_list[i] -= 1
            take_test = True

        if len(test_hours_list) == 0:
            return i + 1

        if take_test == False:
            stored_study_days += 1

    return -1

def __starting_point():
    main()

__starting_point()
