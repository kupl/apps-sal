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
        print('NO')
    else:
        print('YES')


def YESNO(fl):
    if fl:
        print('YES')
    else:
        print('NO')


def main():
    n = iinput()
    q = rlinput()
    w = q.copy()
    if q == sorted(w):
        print(0)
    else:
        res = 1
        for i in range(n):
            if i + 1 == q[i]:
                res = 2
        if res == 1:
            print(1)
        else:
            (l, r) = (0, n - 1)
            for i in range(n):
                if i + 1 != q[i]:
                    l = i
                    break
            for i in range(n - 1, l, -1):
                if i + 1 != q[i]:
                    r = i
                    break
            q = q[l:r + 1]
            n = len(q)
            m = min(q)
            for i in range(n):
                if m + i == q[i]:
                    print(2)
                    return 0
            print(1)


for i in range(iinput()):
    main()
