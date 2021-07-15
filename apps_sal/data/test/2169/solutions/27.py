import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list([int(x) - 1 for x in sys.stdin.readline().rstrip().split()])


# ===CODE===

def main():
    h, w, d = ns()
    pos = dict()
    for i in range(h):
        a = na()
        for j, ai in enumerate(a):
            pos[ai - 1] = (i, j)

    cum = [[0] for _ in range(d)]

    for i in range(d):
        x, y = pos[i]
        num = i + d
        while num < h * w:
            xi, yi = pos[num]
            tmp = abs(xi - x) + abs(yi - y)
            cum[i].append(cum[i][-1] + tmp)
            x, y = xi, yi
            num += d

    q = ni()
    for _ in range(q):
        l, r = ns()
        l, r = l - 1, r - 1
        tmp = cum[l % d][r // d] - cum[l % d][l // d]
        print(tmp)


def __starting_point():
    main()

__starting_point()
