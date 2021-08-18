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


def main():
    n, m = LI()
    l = [LI() for _ in range(m)]
    l = sorted(l, key=lambda x: x[1])

    ans = 1
    kiru = l[0][1] - 0.1
    for x, y in l[1:]:
        if x < kiru < y:
            continue
        ans += 1
        kiru = y - 0.1

    return ans


print((main()))
