#!/usr/bin/env python3

from sys import stdin


def main():
    n, = stdin_get_ints_from_line()
    s = stdin_get_string_from_line()

    res = 0

    for x in s:
        if x == '<':
            res += 1
        else:
            break

    for x in reversed(s):
        if x == '>':
            res += 1
        else:
            break

    print(res)
    return


def stdin_get_ints_from_line():
    return (int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_ints_list_from_line():
    return list(int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_string_from_line():
    return stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
