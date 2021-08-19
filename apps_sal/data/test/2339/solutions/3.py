from math import *
from bisect import *
from collections import *
from random import *
from decimal import *


def inp():
    return int(input())


def st():
    return input().rstrip('\n')


def lis():
    return list(map(int, input().split()))


def ma():
    return list(map(int, input().split()))


t = inp()
while t:
    t -= 1
    n = inp()
    a = lis()
    cur = 0
    r = []
    while len(a) != 0:
        ind = 0
        mi = -1000000000000000
        for i in range(len(a)):
            if gcd(cur, a[i]) > mi:
                mi = gcd(cur, a[i])
                ind = i
        r.append(a[ind])
        cur = gcd(cur, a[ind])
        a.pop(ind)
    print(*r)
