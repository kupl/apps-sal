#!/usr/bin/env python3

from sys import stdin


def main():
    n, = stdin_get_ints_from_line()
    x = stdin_get_ints_list_from_line()

    if x[-1] == 15:
        print('DOWN')
        return

    if x[-1] == 0:
        print('UP')
        return

    if n == 1:
        print('-1')
        return

    if x[-1] > x[-2]:
        print('UP')

    if x[-1] < x[-2]:
        print('DOWN')


def stdin_get_ints_from_line():
    return (int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_ints_list_from_line():
    return list(int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_string_from_line():
    return stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
