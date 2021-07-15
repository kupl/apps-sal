#!/usr/bin/env python3

from sys import stdin


def main():
    n, a = stdin_get_ints_from_line()
    x = stdin_get_ints_list_from_line()
    x.sort()

    if n == 1:
        print(0)
        return

    #print(get_result(a, x[1], x[-1]), get_result(a, x[1], x[-1]))

    print(min(get_result(a, x[1], x[-1]), get_result(a, x[0], x[-2])))


def get_result(a, left, right):
    #print(a, left, right)
    if left < a < right:
        if abs(a-left) < abs(a-right): # go left first
            return (abs(a-left) * 2) + abs(a-right)
        else:
            return abs(a-left) + (abs(a-right) * 2)

    if a <= left:
        return abs(a-right)

    if a >= right:
        return abs(a-left)


def stdin_get_ints_from_line():
    return (int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_ints_list_from_line():
    return list(int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_string_from_line():
    return stdin.readline().strip()


def __starting_point():
    main()

__starting_point()
