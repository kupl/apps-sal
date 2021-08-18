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


def summarizeList(l):
    sl = sorted(l)

    a = sl[0]
    c = 1
    res = []

    for x in sl[1:]:
        if x == a:
            c += 1
        else:
            res.append([a, c])
            a = x
            c = 1
    res.append([a, c])

    return res


def main():
    n, m = LI()
    l = LI()

    rui = [0]
    for x in l:
        y = rui[-1] + x
        rui.append(y % m)

    sl = summarizeList(rui)
    ans = 0
    for x, c in sl:
        ans += c * (c - 1) // 2

    return ans


print((main()))
