import sys
import math
import queue
MOD = 10**9 + 7
sys.setrecursionlimit(1000000)


def hgt(x):
    if x == 0:
        return -1
    h = 0
    while x & 1 != 1:
        h += 1
        x = x >> 1
    return h


def up(x):
    h = hgt(x)
    g = x + (1 << h)
    if g > 0 and g < N and hgt(g) == h + 1:
        return g
    g = x - (1 << h)
    if g > 0 and g < N and hgt(g) == h + 1:
        return g
    return x


def left(x):
    h = hgt(x)
    if h == 0:
        return x
    g = x - (1 << (h - 1))
    if g > 0:
        return g
    return x


def right(x):
    h = hgt(x)
    if h == 0:
        return x
    g = x + (1 << (h - 1))
    if g < N:
        return g
    return x


N, q = map(int, input().split())
N += 1
for _ in range(q):
    p = int(input())
    for c in input():
        if c == 'U':
            p = up(p)
        elif c == 'R':
            p = right(p)
        else:
            p = left(p)
    print(p)
