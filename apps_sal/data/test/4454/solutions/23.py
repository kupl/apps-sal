import io
import sys
import atexit
import os
import math as ma
from decimal import Decimal as dec
from itertools import permutations
from itertools import combinations


def li():
    return list(map(int, sys.stdin.readline().split()))


def num():
    return map(int, sys.stdin.readline().split())


def nu():
    return int(input())


def find_gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


def lcm(x, y):
    gg = find_gcd(x, y)
    return x * y // gg


mm = 1000000007


def solve():
    t = nu()
    for tt in range(t):
        n = nu()
        a = li()
        s = sum(a)
        print(int(ma.ceil(s / n)))


def __starting_point():
    solve()


__starting_point()
