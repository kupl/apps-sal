# AtCoder Beginner Contest 148
# F - Playing Tag on Tree
# https://atcoder.jp/contests/abc148/tasks/abc148_f
from collections import deque

import sys
input = sys.stdin.readline
N, U, V = list(map(int, input().split()))
U -= 1
V -= 1
G = [[] for _ in [0] * N]
for _ in [0] * (N - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

INF = 10**10

T = [INF] * N
T[U] = 0
A = [INF] * N
A[V] = 0


def bfs(v, dist):
    q = deque()
    q.append(v)
    k = 0
    visited = [0] * N
    while q:
        v = q.popleft()
        visited[v] = 1
        k = dist[v]

        for u in G[v]:
            if visited[u]:
                continue
            q.append(u)
            dist[u] = k + 1


bfs(U, T)
bfs(V, A)

if A[U] <= 1:
    print((0))
    return

farthest = 0
node = -1
for i, (t, a) in enumerate(zip(T, A)):
    if t < a and farthest < a:
        farthest = a
        node = i

print((farthest - 1))
