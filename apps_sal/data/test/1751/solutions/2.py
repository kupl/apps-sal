import sys
import random
from math import *


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
    return map(int, tinput())


def fiinput():
    return map(float, tinput())


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


def main():
    n = iinput()
    res, ans, mod = 1, 1, int(1e9 + 7)
    for i in range(1, n + 1):
        res = res * i % mod
    for i in range(1, n):
        ans = ans * 2 % mod
    print((res - ans + mod) % mod)


for inytd in range(1):
    main()
