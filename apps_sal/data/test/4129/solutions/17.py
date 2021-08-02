# -*- coding: utf-8 -*-

import sys
from collections import Counter


def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


INF = 10 ** 18
MOD = 10 ** 9 + 7


def bfs(nodes, src):
    from collections import deque

    que = deque([(src, 0)])
    dist[src][src] = 1
    while que:
        u, c = que.popleft()
        for v in nodes[u]:
            if dist[src][v]:
                continue
            dist[src][v] = 1
            que.append((v, c + 1))


N, M, s = MAP()
s -= 1

nodes = [[] for i in range(N)]
for _ in range(M):
    a, b = MAP()
    a -= 1; b -= 1
    nodes[a].append(b)

dist = list2d(N, N, 0)
for i in range(N):
    bfs(nodes, i)

need = []
for v in range(N):
    if not dist[s][v]:
        need.append((dist[v].count(1), v))
need.sort(reverse=1)

done = [False] * N
ans = 0
for _, u in need:
    if not done[u]:
        for v, can in enumerate(dist[u]):
            if can:
                done[v] = True
        ans += 1
print(ans)
