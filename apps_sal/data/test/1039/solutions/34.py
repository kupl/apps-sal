from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)
n = int(input())
g = [[] for i in range(n)]
for i in range(n - 1):
    (a, b, c) = list(map(int, input().split()))
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, c))
(q, k) = list(map(int, input().split()))
dist = [-1] * n


def dfs(st, depth=0):
    dist[st] = depth
    for (to, c) in g[st]:
        if dist[to] >= 0:
            continue
        dfs(to, depth + c)


dfs(k - 1, 0)
for i in range(q):
    (x, y) = list(map(int, input().split()))
    x -= 1
    y -= 1
    print(dist[x] + dist[y])
