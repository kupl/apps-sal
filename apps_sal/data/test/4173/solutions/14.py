import io
import sys
import atexit
import os


import math as ma
from decimal import Decimal as dec
from itertools import permutations


def li():
    return list(map(int, input().split()))


def num():
    return map(int, input().split())


def nu():
    return int(input())


def find_gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


def solve():
    t = nu()
    for it in range(t):
        n, a, b = num()
        x = 0
        if(n % 2 == 0):
            x = n // 2 * b
        else:
            x = n // 2 * b + a
        y = n * a
        print(min(x, y))


def __starting_point():
    solve()


__starting_point()
