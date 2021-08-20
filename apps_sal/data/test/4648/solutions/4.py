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
    (t, g) = (0, 0)
    while n % 3 == 0:
        g += 1
        n //= 3
    while n % 2 == 0:
        n //= 2
        t += 1
    if n != 1 or t > g:
        print(-1)
    else:
        print(g * 2 - t)


for inytd in range(iinput()):
    main()
