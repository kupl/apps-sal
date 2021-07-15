import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v, p):
        for u in edge_extend[p][v]:
            next_p = 0 if p == 2 else p + 1
            if dist[next_p][u] <= dist[p][v] + 1:
                continue
            else:
                dist[next_p][u] = dist[p][v] + 1
                dfs(u, next_p)

    n, m = list(map(int, input().split()))
    edge = [[] for _ in range(n)]
    for _ in range(m):
        u, v = list(map(int, input().split()))
        edge[u - 1].append(v - 1)
    s, t = list(map(int, input().split()))

    edge_extend = []
    for _ in range(3):
        edge_extend.append(edge)

    dist = [[f_inf] * n for _ in range(3)]
    dist[0][s - 1] = 0
    que = deque([[0, s - 1]])
    while que:
        p, v = que.popleft()
        next_p = 0 if p == 2 else p + 1
        for u in edge_extend[p][v]:
            if dist[next_p][u] > dist[p][v] + 1:
                dist[next_p][u] = dist[p][v] + 1
                que.append([next_p, u])

    print((dist[0][t - 1] // 3 if dist[0][t - 1] != f_inf else -1))


def __starting_point():
    resolve()

__starting_point()
