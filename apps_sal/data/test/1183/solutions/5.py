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
    return list(map(int, sys.stdin.readline().split()))


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
        (n, x) = num()
        a = li()
        s = set(a)
        cc = 1
        while x != 0:
            if cc in s:
                cc += 1
                continue
            x -= 1
            s.add(cc)
            cc += 1
        cc = 1
        pp = 0
        while cc in s:
            pp += 1
            cc += 1
        print(pp)


def __starting_point():
    solve()


__starting_point()
