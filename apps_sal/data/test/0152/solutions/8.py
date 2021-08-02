#!/usr/bin/env python3

from sys import stdin
from bisect import bisect_right


def main():
    n, m, k = stdin_get_ints_from_line()  # amount to brew, first cast count, second cask count 2*10^9, 2*10^5, 2*10^5
    x, s = stdin_get_ints_from_line()  # time to brew, mana amount

    a = stdin_get_ints_list_from_line()  # time to brew with ai first cast 2*10^9
    b = stdin_get_ints_list_from_line()  # cost of first cast 2*10^9
    c = stdin_get_ints_list_from_line()  # amount to brew instantly 2*10^9
    d = stdin_get_ints_list_from_line()  # cost of second cast 2*10^9

    result = n * x

    key = bisect_right(d, s)

    if key != 0:
        spell2_only_result = (n - c[key - 1]) * x
        if spell2_only_result < result:
            result = spell2_only_result

    for key, val in enumerate(b):
        if val <= s:
            if a[key] < x:
                cost_left = s - val
                amount_second = 0

                key2 = bisect_right(d, cost_left)

                if key2 != 0:
                    amount_second = c[key2 - 1]

                r = (n - amount_second) * a[key]

                if r < result:
                    result = r
                if result <= 0:
                    break

    print(result) if result > 0 else print(0)


def stdin_get_ints_from_line():
    return (int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_ints_list_from_line():
    return list(int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_string_from_line():
    return stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
