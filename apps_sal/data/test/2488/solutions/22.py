import sys
# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
# import heapq
import decimal
# import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: list(map(int, sys.stdin.readline().split()))
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    n, d, a = ns()
    x = []
    for _ in range(n):
        xi, hi = ns()
        x.append([xi, hi])

    x.sort()
    x.append([INF, INF])

    perm = [0 for _ in range(n + 1)]
    idx = [xi for xi, hi in x]

    ans = 0
    cnt = 0
    for i in range(n):
        cnt -= perm[i]

        if x[i][1] - cnt * a > 0:
            tmp = ((x[i][1] - cnt * a) + a - 1) // a
        else:
            continue
        ans += tmp
        cnt += tmp

        if cnt > 0:
            tmp_idx = bisect.bisect_right(idx, x[i][0] + 2 * d)
            perm[tmp_idx] += tmp

    print(ans)


def __starting_point():
    main()

__starting_point()
