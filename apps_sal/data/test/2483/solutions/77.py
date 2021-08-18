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
    N, C = LI()
    l = [[0] * 100100 for _ in range(C)]

    for _ in range(N):
        s, t, c = LI()
        l[c - 1][s] += 1
        l[c - 1][t + 1] -= 1

    for i in range(C):
        for j in range(100000):
            l[i][j + 1] += l[i][j]

    for i in range(C):
        for j in range(100000):
            if l[i][j] == 2:
                l[i][j] = 1

    mx = 0
    for i in range(100000):
        sm = 0
        for j in range(C):
            sm += l[j][i]
        mx = max(mx, sm)

    return mx


print((main()))
