from collections import deque

n, m = list(map(int, input().split()))
uv = [list(map(int, input().split())) for _ in range(m)]
s, t = list(map(int, input().split()))

adj = [[] for _ in range(3 * n)]
for u, v in uv:
    u -= 1
    v -= 1
    adj[u].append(v + n)
    adj[u + n].append(v + 2 * n)
    adj[u + 2 * n].append(v)


def bfs(s):
    q = deque([s])
    d = [-1] * (3 * n)
    d[s] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                q.append(v)

    return d


dist = bfs(s - 1)
ans = dist[t - 1]
print((ans // 3))

