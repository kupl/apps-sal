import io
import sys
import atexit
import os
import math as ma
from decimal import Decimal as dec
from itertools import permutations
from itertools import combinations


def li():
    return list(map(int, input().split()))


def num():
    return map(int, input().split())


def nu():
    return int(input())


def find_gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


def prod(n):
    s = 1
    while n != 0:
        s = s * (n % 10)
        n = n // 10
    return s


def check(xp):
    op = sorted(xp)
    if op == xp:
        return True


mm = 1000000007


def solve():
    t = 1
    for it in range(t):
        n = nu()
        xp = [15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 16, 17]
        print(xp[n])
        continue


def __starting_point():
    solve()


__starting_point()
