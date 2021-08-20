import sys
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


def srlinput():
    return sorted(list(map(int, input().split())))


def main():
    n = iinput()
    q = rlinput()
    b = dict()
    o = 0
    for i in rlinput():
        b[i] = o
        o += 1
    res = [0 for i in range(n)]
    for i in range(n):
        res[i] = b[q[i]] - i
        if res[i] < 0:
            res[i] += n
    f = dict()
    for i in res:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    z = 0
    for (i, v) in f.items():
        z = max(z, v)
    print(z)


for inytd in range(1):
    main()
