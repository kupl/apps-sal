import io, sys, atexit, os
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
    while (y):
        x, y = y, x % y
    return x


def lcm(x, y):
    gg = find_gcd(x, y)
    return (x * y // gg)


mm = 1000000007


def solve():
    t = nu()
    for tt in range(t):
        a,b=num()
        if(a<=b):
            dd=b-a
            pq=dd//5
            yp=dd%5
            yo=yp//2
            yu=yp%2
            print(pq+yu+yo)
        else:
            a,b=b,a
            dd = b - a
            pq = dd // 5
            yp = dd % 5
            yo = yp // 2
            yu = yp % 2
            print(pq + yu + yo)


def __starting_point():
    solve()
__starting_point()
