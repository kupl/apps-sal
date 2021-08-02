import io
import sys
import atexit
import os

import math as ma
from decimal import Decimal as dec
from itertools import permutations
from random import randint as rand


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


def lcm(x, y):
    gg = find_gcd(x, y)
    return (x * y // gg)


mm = 1000000007
yp = 0


def solve():
    t = 1
    for _ in range(t):
        n, m, r = num()
        a = li()
        b = li()
        a.sort()
        b.sort()
        pq = r // a[0]
        print(max(pq * b[m - 1] + r % a[0], r))


def __starting_point():
    solve()


__starting_point()
