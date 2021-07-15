from collections import deque

def bfs(s, t):
    dist = [-1] * (3 * n + 1)
    q = deque()
    q.append(s)
    dist[s] = 0
    while q:
        p = q.popleft()
        for i in G[p]:
            if dist[i] == -1:
                dist[i] = dist[p] + 1
                q.append(i)
    return dist[t]

n, m = map(int, input().split())
G = [[] for _ in range(3 * n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v + n)
    G[u + n].append(v + 2 * n)
    G[u + 2 * n].append(v)
s, t = map(int, input().split())
ans = bfs(s, t)
print(ans // 3 if not ans == -1 else ans)
