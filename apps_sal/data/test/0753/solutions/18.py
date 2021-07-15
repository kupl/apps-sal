#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Vitaly Pavlenko

import random
from fractions import gcd


def average(x):
    return sum(x) / len(x)


def shuffled(a):
    a = list(a)
    random.shuffle(a)
    return a


def read_ints():
    return [int(i) for i in input().split()]


def decrease(a):
    return [i - 1 for i in a]




def main():
    # nonlocal input
    # nonlocal print

    # fin = open('input.txt', 'r')
    # input = lambda: fin.readline().strip()
    # fout = open('output.txt', 'w')
    # _print = print
    # print = lambda *args, **kwargs: _print(*args, file=fout, **kwargs)

    a, b, c, d = read_ints()

    if a / b < c / d:
        a, b, c, d = b, a, d, c

    p, q = a * d - c * b, b * d
    s, t = p, a * d
    print(s // gcd(s, t), t // gcd(s, t), sep='/')

    # fout.close()


def __starting_point():
    # import doctest
    # doctest.testmod()
    main()
__starting_point()
