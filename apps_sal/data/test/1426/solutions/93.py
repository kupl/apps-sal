import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    (n, m) = list(map(int, input().split()))
    edge = [[] for _ in range(n)]
    for _ in range(m):
        (u, v) = list(map(int, input().split()))
        edge[u - 1].append(v - 1)
    (s, t) = list(map(int, input().split()))
    dist = [[f_inf] * 3 for _ in range(n)]
    que = deque([])
    que.append([s - 1, 0])
    dist[s - 1][0] = 0
    while que:
        (v, l) = que.popleft()
        for u in edge[v]:
            nl = (l + 1) % 3
            if dist[u][nl] == f_inf:
                dist[u][nl] = dist[v][l] + 1
                que.append([u, nl])
    res = dist[t - 1][0]
    print(-1 if res == f_inf else res // 3)


def __starting_point():
    resolve()


__starting_point()
