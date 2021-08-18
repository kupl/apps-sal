import sys
import random
from fractions import Fraction
from math import *
from decimal import *


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def finput():
    return float(input())


def tinput():
    return input().split()


def linput():
    return list(input())


def rinput():
    return list(map(int, tinput()))


def fiinput():
    return list(map(float, tinput()))


def rlinput():
    return list(map(int, input().split()))


def trinput():
    return tuple(rinput())


def srlinput():
    return sorted(list(map(int, input().split())))


def NOYES(fl):
    if fl:
        print("NO")
    else:
        print("YES")


def YESNO(fl):
    if fl:
        print("YES")
    else:
        print("NO")


def modst(a, s):
    res = 1
    while s:
        if s % 2:
            res = res * a % 998244353
        a *= a
        a = a % 998244353
        s //= 2
    return res


def main():
    n, k = rinput()
    q = srlinput()
    res = 0
    for i in range(1, n):
        res += (k - q[i]) // q[0]
    print(res)


for i in range(iinput()):
    main()
