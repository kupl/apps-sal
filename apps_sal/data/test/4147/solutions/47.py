import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys
import queue
import copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()


n, a, b, c = LI()
l = [I() for _ in range(n)]


def dfs(cnt, aa, bb, cc):
    if cnt == n:
        if aa == 0 or bb == 0 or cc == 0:
            return inf
        return abs(aa - a) + abs(bb - b) + abs(cc - c) - 30

    aaa = dfs(cnt + 1, aa + l[cnt], bb, cc) + 10
    bbb = dfs(cnt + 1, aa, bb + l[cnt], cc) + 10
    ccc = dfs(cnt + 1, aa, bb, cc + l[cnt]) + 10
    ddd = dfs(cnt + 1, aa, bb, cc)
    return min(aaa, bbb, ccc, ddd)


print((dfs(0, 0, 0, 0)))
