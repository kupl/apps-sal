import sys
import math
from math import ceil
import bisect


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def finput():
    return float(input())


def tinput():
    return input().split()


def rinput():
    return map(float, tinput())


def rlinput():
    return list(rinput())


def sli():
    return set(list(input()))


def modst(a, s):
    res = 1
    while s:
        if s % 2:
            res *= a
        a *= a
        s //= 2
    return res


def pro(x):
    if x < 37:
        return (x - 1) // 4
    else:
        return 8 - (x - 37) // 2


def main():
    q = sli()
    w = sli()
    flag = False
    for i in q:
        if i in w:
            flag = True
            break
    if flag:
        print('YES')
    else:
        print('NO')


for i in range(iinput()):
    main()
