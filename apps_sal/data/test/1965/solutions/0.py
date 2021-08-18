import sys
import random
from fractions import Fraction
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


def main():
    n, k = rinput()
    q = srlinput()
    print((q.count(k) != n) * (k in q) + (1 + (k * n != sum(q))) * (k not in q))


for i in range(iinput()):
    main()
