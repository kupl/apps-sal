from collections import deque
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, m, *uv, s, t = list(map(int, read().split()))
m = iter(uv)
UV = list(zip(m, m))
graph = [[] for _ in range(3 * n)]
for u, v in UV:
    u -= 1
    v -= 1
    graph[u].append(v + n)
    graph[u + n].append(v + 2 * n)
    graph[u + 2 * n].append(v)
s -= 1
t -= 1
infi = 10 ** 20
dist = [-1] * (3 * n)


def bfs(s):
    que = deque()
    dist[s] = 0
    que.append(s)
    while que:
        v = que.popleft()
        if v == t:
            return dist[t]
        d = dist[v]
        for u in graph[v]:
            if dist[u] > 0:
                continue
            dist[u] = d + 1
            que.append(u)
    return -1


ans = bfs(s)
if ans > 0:
    ans //= 3
print(ans)

