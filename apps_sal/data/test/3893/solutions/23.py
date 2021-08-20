import collections
import itertools
import functools
import math


def value(a, b, c, x, y):
    return a * x + b * y + c


def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    if x > 0:
        return 1


def solve():
    (x1, y1) = list(map(int, input().split()))
    (x2, y2) = list(map(int, input().split()))
    n = int(input())
    r = 0
    for i in range(n):
        (a, b, c) = list(map(int, input().split()))
        s1 = value(a, b, c, x1, y1)
        s2 = value(a, b, c, x2, y2)
        if sign(s1) != sign(s2):
            r += 1
    return r


def __starting_point():
    print(solve())


__starting_point()
