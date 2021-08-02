#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools


def divceil(a, b):
    return (a + b - 1) // b


def solve(h1, h2, a, b):
    if a - b <= 0:
        return 0 if divceil(h2 - h1, a) <= 8 else -1
    h = h1
    h += a * 8
    if h >= h2:
        return 0
    h -= b * 12
    for i in itertools.count(1):
        h += a * 12
        if h >= h2:
            return i
        h -= b * 12


def main():
    h1, h2 = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    print(solve(h1, h2, a, b))


def __starting_point():
    main()


__starting_point()
