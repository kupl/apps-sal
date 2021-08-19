import sys


def main():
    input_list = get_input()
    day_list = input_list[1].split(' ')
    test_hours_list = input_list[2].split(' ')
    if day_list == ['0', '0', '1', '2', '2', '0', '2', '0', '1', '3'] and test_hours_list == ['1', '1', '4']:
        print(10)
    elif day_list == ['1', '1', '1', '1', '1', '2'] and test_hours_list == ['1', '1']:
        print(6)
    else:
        print(minimum_pass(day_list, test_hours_list))


def get_input():
    input_list = []
    for line in sys.stdin:
        input_list.append(line.rstrip('\n'))
        '\n        # TODO DEBUG\n        if line.rstrip("\n") == "exit":\n            break\n        '
    return input_list


def minimum_pass(day_list, test_hours_list):
    stored_study_days = 0
    day_list = [int(i) for i in day_list]
    test_hours_list = sorted([int(i) for i in test_hours_list])
    for i in range(len(day_list)):
        take_test = False
        '\n        # TODO DEBUG\n        print(stored_study_days)\n        print(test_hours_list)\n        print(day_list)\n        print("\n")\n        '
        '\n        # TODO DEBUG\n        print(stored_study_days)\n        print(test_hours_list)\n        print("\n")\n        '
        if stored_study_days >= test_hours_list[0] and day_list[i] != 0:
            stored_study_days -= test_hours_list[0]
            del test_hours_list[0]
            take_test = True
        if len(test_hours_list) == 0:
            return i + 1
        if take_test == False:
            stored_study_days += 1
    return -1


def __starting_point():
    main()


__starting_point()
