import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict


def VI(): return list(map(int, input().split()))
def I(): return int(input())
def LIST(n, m=None): return [0] * n if m is None else [[0] * m for i in range(n)]
def ELIST(n): return [[] for i in range(n)]


def MI(n=None, m=None):
    if n is None:
        n, m = VI()
    arr = LIST(n)
    for i in range(n):
        arr[i] = VI()
    return arr


def MS(n=None, m=None):
    if n is None:
        n, m = VI()
    arr = LIST(n)
    for i in range(n):
        arr[i] = input()
    return arr


def MIT(n=None, m=None):
    if n is None:
        n, m = VI()
    arr = LIST(m, n)
    for i in range(n):
        v = VI()
        for j in range(m):
            arr[j][i] = v[j]
    return arr


def run2(n, m, u, v, w, x):
    g = ELIST(n + 1)
    for i in range(m):
        g[u[i]].append((v[i], w[i], i + 1))
        g[v[i]].append((u[i], w[i], i + 1))
    pq = []
    marked = [False] * (n + 1)
    pq.append((0, 0, x, 0))
    sg = []
    wmax = -w[-1]
    while len(pq) != 0:
        wi, lw, i, ei = heapq.heappop(pq)
        if not marked[i]:
            marked[i] = True
            sg.append(ei)
            wmax += w[ei - 1]
            for j, wj, ej in g[i]:
                if not marked[j]:
                    heapq.heappush(pq, (wi + wj, wj, j, ej))
    sg = sg[1:]
    print(wmax)
    for i in sg:
        print(i, end=" ")
    print()


def main2(info=0):
    n, m = VI()
    u, v, w = MIT(m, 3)
    x = I()
    run(n, m, u, v, w, x)


def run(n, m, g, x):
    pq = [(0, 0, x, 0)]
    marked = [False] * (n + 1)
    sg = []
    wtot = 0
    while len(pq) != 0:
        wi, lw, i, ei = heapq.heappop(pq)
        if not marked[i]:
            marked[i] = True
            sg.append(str(ei))
            wtot += lw
            for j, wj, ej in g[i]:
                if not marked[j]:
                    heapq.heappush(pq, (wi + wj, wj, j, ej))
    print(wtot)
    print(" ".join(sg[1:]))


def main(info=0):
    n, m = VI()
    g = ELIST(n + 1)
    for i in range(m):
        u, v, w = VI()
        g[u].append((v, w, i + 1))
        g[v].append((u, w, i + 1))
    x = I()
    run(n, m, g, x)


def __starting_point():
    main()


__starting_point()
