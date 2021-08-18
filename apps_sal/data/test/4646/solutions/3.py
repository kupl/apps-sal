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
    n = iinput()
    q = rlinput()
    t = 0
    for i in range(n):
        q[i] %= 2
        if q[i] != i % 2:
            t += 1
    if sum(q) != n // 2:
        print(-1)
    else:
        print(t // 2)


for inytd in range(iinput()):
    main()
