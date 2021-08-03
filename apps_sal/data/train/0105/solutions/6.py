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
    #n = iinput()
    #k = iinput()
    #m = iinput()
    #n = int(sys.stdin.readline().strip())
    n, k = rinput()
    #n, m = rinput()
    #m, k = rinput()
    #n, k, m = rinput()
    #n, m, k = rinput()
    #k, n, m = rinput()
    #k, m, n = rinput()
    #m, k, n = rinput()
    #m, n, k = rinput()
    q = srlinput()
    #q = linput()
    res = 0
    for i in range(1, n):
        res += (k - q[i]) // q[0]
    print(res)


for i in range(iinput()):
    main()
