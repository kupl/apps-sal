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
    while (y):
        x, y = y, x % y
    return x


def lcm(x, y):
    gg = find_gcd(x, y)
    return (x * y // gg)


def printDivisors(n):
    i = 1
    cc = 0
    while i <= ma.sqrt(n):

        if (n % i == 0):

            if (n / i == i):
                cc += 1
            else:
                cc += 2
        i = i + 1
    return cc


mm = 1000000007
yp = 0


def solve():
    t = 1
    for tt in range(t):
        n = nu()
        a = li()
        gg = 0
        for i in range(n):
            gg = find_gcd(gg, a[i])
        cc = 0
        print(printDivisors(gg))


def __starting_point():
    solve()


__starting_point()
