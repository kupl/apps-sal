import sys


def resolve(in_):
    S = next(in_).strip()
    _weekday = {0: 'SUN', 1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT'}
    weekday = {v: 7 - k for (k, v) in list(_weekday.items())}
    return weekday[S]


def main():
    answer = resolve(sys.stdin)
    print(answer)


def __starting_point():
    main()


__starting_point()
