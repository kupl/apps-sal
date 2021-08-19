import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():

    def bfs(start):
        dist = [f_inf] * n
        dist[start] = 0
        que = deque([start])
        while que:
            v = que.popleft()
            for u in edge[v]:
                if dist[u] == f_inf:
                    dist[u] = dist[v] + 1
                    que.append(u)
        return dist
    (n, u, v) = list(map(int, input().split()))
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        (a, b) = list(map(int, input().split()))
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    distA = bfs(u - 1)
    distT = bfs(v - 1)
    res = 0
    for i in range(n):
        if distA[i] < distT[i]:
            res = max(res, distT[i])
    print(res - 1)


def __starting_point():
    resolve()


__starting_point()
