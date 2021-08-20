from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [False] * n
    visited[0] = True
    color = [-1] * n
    color[0] = 1
    q = deque([(0, 1, -1)])
    while q:
        (v, pre_c1, pre_c2) = q.popleft()
        cnt = 1
        for nv in G[v]:
            if visited[nv]:
                continue
            while cnt == pre_c1 or cnt == pre_c2:
                cnt += 1
            color[nv] = cnt
            cnt += 1
            q.append((nv, color[v], color[nv]))
            visited[nv] = True
    return color


n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    (x, y) = map(int, input().split())
    G[x - 1].append(y - 1)
    G[y - 1].append(x - 1)
color = bfs()
print(max(color))
print(*color)
