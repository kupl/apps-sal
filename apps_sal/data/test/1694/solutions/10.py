import sys
from itertools import *
from math import *


def solve():
    (n, m, s, f) = map(int, input().split())
    s -= 1
    f -= 1
    d = {}
    for _ in range(m):
        (t, l, r) = map(int, input().split())
        d[t - 1] = (l - 1, r - 1)
    step = 0
    res = ''
    while s != f:
        wantnext = s + 1 if s < f else s - 1
        canmove = True
        if step in d:
            (l, r) = d[step]
            if s >= l and s <= r or (wantnext >= l and wantnext <= r):
                canmove = False
        if canmove:
            res += 'R' if wantnext > s else 'L'
            s = wantnext
        else:
            res += 'X'
        step += 1
    print(res)


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
solve()
