#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
from collections import defaultdict
INF = float("inf")
MOD = 10**9+7


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, f, t, w=1):
        self.E[f].append(t)
        self.E[t].append(f)


def make_order(g, v):
    seen = [False]*g.N
    last_order = [-1]*g.N
    parent = [-1]*g.N
    size = [1]*g.N
    counter = {"last": 0}

    def recur(v):
        seen[v] = True
        for to in g.E[v]:
            if seen[to] == True:
                continue
            parent[to] = v
            recur(to)
            size[v] += size[to]

        last_order[counter["last"]] = v
        counter["last"] += 1

    recur(v)
    return last_order, parent, size


def merge(d: dict, e: dict):
    if len(d) < len(e):
        d, e = e, d
    for k in e:
        d[k] += e[k]
    return d


N = int(input())
c = [x-1 for x in map(int, input().split())]
A = [None]*(N-1)
B = [None]*(N-1)
for i in range(N-1):
    A[i], B[i] = list(map(int, input().split()))

g = Graph(N)
for a, b in zip(A, B):
    g.add_edge(a-1, b-1)

ans = [0]*N

ret = {}
last_order, parent, size = make_order(g, 0)
for curr in last_order:
    cn = c[curr]
    rrr = defaultdict(int)
    for dest in g.E[curr]:
        if dest == parent[curr]:
            continue
        child = ret.pop(dest)

        n = size[dest]-child[cn]
        ans[cn] += n*(n+1)//2

        # マージ
        rrr = merge(rrr, child)

    rrr[cn] = size[curr]
    ret[curr] = rrr


tot = N*(N+1)//2
for color in range(N):
    if color != c[0]:
        n = N-ret[0][color]
        ans[color] += n*(n+1)//2
    print((tot-ans[color]))

