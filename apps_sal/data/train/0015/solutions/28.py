#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=tf-8
#

"""
"""

from operator import itemgetter
from collections import Counter


def solve(a, b, x, y):
    area1 = x * b
    area2 = (a - x - 1) * b
    area3 = a * y
    area4 = a * (b - y - 1)
    print(max(area1, area2, area3, area4))


def main():
    t = int(input())
    for i in range(t):
        a, b, x, y = map(int, input().split())
        solve(a, b, x, y)


def __starting_point():
    main()


__starting_point()
