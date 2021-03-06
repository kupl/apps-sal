import re
import copy
import random
import decimal
import heapq
import itertools
import bisect
import collections
import math
import sys
production = True


def input(f=0, m=0):
    if m > 0:
        return [input(f) for i in range(m)]
    else:
        l = sys.stdin.readline()[:-1]
        if f >= 10:
            u = False
            f = int(str(f)[-1])
        else:
            u = True
        if f == 0:
            p = [l]
        elif f == 1:
            p = list(map(int, l.split()))
        elif f == 2:
            p = list(map(float, l.split()))
        elif f == 3:
            p = list(l)
        elif f == 4:
            p = list(map(int, list(l)))
        elif f == 5:
            p = l.split()
        return p if u else p[0]


def out(l, f=0, n=True):
    if f == 0:
        p = str(l)
    elif f == 1:
        p = ' '.join(map(str, l))
    elif f == 2:
        p = '\n'.join(map(str, l))
    elif f == 3:
        p = ''.join(map(str, l))
    print(p, end='\n' if n else '')


def log(*args):
    if not production:
        print('$$$', end='')
        print(*args)


enu = enumerate


def ter(a, b, c):
    return b if a else c


def ceil(a, b):
    return -(-a // b)


def mapl(i, f=0):
    if f == 0:
        return list(map(int, i))
    elif f == 1:
        return list(map(str, i))
    elif f == 2:
        return list(map(list, i))


def solve():
    (n, m) = input(1)
    a = input(3, n)
    t = 0
    for i in a[-1]:
        if i == 'D':
            t += 1
    for i in range(n):
        if a[i][-1] == 'R':
            t += 1
    out(t)
    log()
    return


for i in range(input(11)):
    solve()
