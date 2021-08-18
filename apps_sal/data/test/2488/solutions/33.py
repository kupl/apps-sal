import sys
import math
import collections
import bisect
import itertools
import fractions
import copy
import decimal
import queue


sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))


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
            tmp = 0
        ans += tmp
        cnt += tmp

        if cnt > 0:
            tmp_idx = bisect.bisect_right(idx, x[i][0] + 2 * d)
            perm[tmp_idx] += tmp

    print(ans)


def __starting_point():
    main()


__starting_point()
