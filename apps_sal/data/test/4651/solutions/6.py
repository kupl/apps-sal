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
        b = [0] * n
        for i in range(1, n + 1):
            ind = -1
            for j in range(n):
                if a[j] == i:
                    ind = j
                    break
            while ind > 0:
                oz = ind - 1
                if b[oz] == 1:
                    break
                if a[oz] < a[ind]:
                    break
                b[oz] = 1
                (a[oz], a[ind]) = (a[ind], a[oz])
                ind -= 1
        print(*a)


def __starting_point():
    solve()


__starting_point()
