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


def YESNO(fl):
    if fl:
        print("NO")
    else:
        print("YES")


def main():
    a, b, n = rinput()
    g = 0
    a, b = sorted([a, b])
    while b <= n:
        a += b
        g += 1
        if a > n:
            break
        b += a
        g += 1
    print(g)


for inytd in range(int(input())):
    main()
