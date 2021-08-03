#!/usr/bin/env python3

from sys import stdin


def main():
    x, y = stdin_get_ints_from_line()

    for _ in range(y):
        if str(x).endswith('0'):
            x = x // 10
        else:
            x = x - 1

    print(x)


def stdin_get_ints_from_line():
    return (int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_ints_list_from_line():
    return list(int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_string_from_line():
    return stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
