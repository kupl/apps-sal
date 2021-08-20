from bisect import *
import math
import itertools
from heapq import *
from collections import *
import sys
sys.setrecursionlimit(10000000)


def input():
    return sys.stdin.readline()[:-1]


INF = 10 ** 9
MOD = 10 ** 9 + 7
(N, M) = map(int, input().split())
es = [[] for i in range(N + 1)]
for i in range(M):
    (a, b) = map(int, input().split())
    es[a].append(b)
(ansr, ansd) = (-1, INF)
for r in range(1, N + 1):
    d = [INF] * (N + 1)
    d[0] = 0
    dq = deque()
    for w in es[r]:
        dq.append(w)
        d[w] = 1
    while len(dq) > 0:
        v = dq.popleft()
        if v == r:
            break
        nd = d[v] + 1
        for u in es[v]:
            if nd < d[u]:
                d[u] = nd
                dq.append(u)
    if d[r] < ansd:
        ansd = d[r]
        ansr = r
if ansr == -1:
    print(-1)
else:
    vis = [0] * (N + 1)
    vis[0] = 1
    p = [-1] * (N + 1)
    dq = deque()
    for v in es[ansr]:
        vis[v] = 1
        p[v] = 0
        dq.append(v)
    while len(dq) > 0:
        v = dq.popleft()
        if v == ansr:
            break
        for u in es[v]:
            if vis[u] == 0:
                vis[u] = 1
                p[u] = v
                dq.append(u)
    lst = []
    v = ansr
    while p[v] != -1:
        lst.append(v)
        v = p[v]
    print(len(lst))
    print(*lst, sep='\n')
