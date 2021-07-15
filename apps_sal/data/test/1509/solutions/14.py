#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Codeforces Round #553 (Div. 2)

Problem E. Number of Components

:author:         Kitchen Tong
:mail:    kctong529@gmail.com

Please feel free to contact me if you have any question
regarding the implementation below.
"""

__version__ = '1.0'
__date__ = '2019-04-20'

import sys


def count_contribution(n, ax, ay):
    if ay > ax:
        return (ay - ax) * (n - ay + 1)
    elif ay < ax:
        return ay * (ax - ay)
    else:
        return 0

def solve(n, a):
    result = a[0] * (n - a[0] + 1)
    for i in range(1, len(a)):
        result += count_contribution(n, a[i-1], a[i])
    return result


def main(argv=None):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
    return 0


def __starting_point():
    STATUS = main()
    return(STATUS)


__starting_point()
