#!/usr/bin/env python3
# coding: utf-8
# Last Modified: 24/Dec/19 08:08:49 PM


import sys


def main():
    for tc in range(int(input())):
        a, b, c, r = get_ints()

        if a > b:
            a, b = b, a

        arr = [c - r, c + r]

        ans = 0

        if a > c + r:
            print(abs(b - a))
            continue

        if b < c - r:
            print(abs(b - a))
            continue

        if a < c - r:
            ans += abs(a - (c - r))

        if b > c + r:
            ans += abs(b - (c + r))

        print(ans)


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
