import math as ma
import sys
from decimal import Decimal as dec
from itertools import permutations


def li():
    return list(map(int, input().split()))


def num():
    return list(map(int, input().split()))


def nu():
    return int(input())


def find_gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


(n, t) = num()
a = li()
count = n
z = 0
while count > 0 and sum(a) > 0:
    pp = 0
    z += t // sum(a) * count
    t = t % sum(a)
    for i in range(n):
        if t >= a[i] and a[i] != 0:
            pp += 1
            t -= a[i]
        else:
            a[i] = 0
    count = pp
    z += pp
print(z)
