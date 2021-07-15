#!/usr/bin/env python3
# coding: utf-8
# Last Modified: 28/Dec/19 10:36:05 PM


import sys


def main():
    x = 24 * 60
    for tc in range(int(input())):
        h, m = get_ints()
        y = h * 60 + m
        print(x - y)


get_array = lambda: list(map(int, sys.stdin.readline().split()))


get_ints = lambda: list(map(int, sys.stdin.readline().split()))


input = lambda: sys.stdin.readline().strip()


def __starting_point():
    main()

__starting_point()
