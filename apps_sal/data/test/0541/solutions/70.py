import sys
import math
import collections
import bisect
import copy

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: list(map(int, sys.stdin.readline().split()))
na = lambda: list(map(int, sys.stdin.readline().split()))
na1 = lambda: list([int(x) - 1 for x in sys.stdin.readline().split()])


# ===CODE===


def main():
    n, m = ns()
    d = []
    for _ in range(m):
        a, b = ns()
        d.append([a - 1, b - 1])

    d.sort(key=lambda x: x[1])

    down = []

    for a, b in d:
        idx = bisect.bisect_left(down, a)
        if idx == len(down):
            down.append(b - 1)
    print((len(down)))


def __starting_point():
    main()

__starting_point()
