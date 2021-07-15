from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    dist = [-1] * (n + 1)
    dist[s] = 0
    while q:
        p = q.popleft()
        for i in G[p]:
            if dist[i] == -1:
                dist[i] = dist[p] + 1
                q.append(i)
    return dist

n, u, v = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
dist1 = bfs(u)
dist2 = bfs(v)
ans = 0
for i in range(1, n + 1):
    if dist1[i] <= dist2[i]:
        ans = max(ans, dist2[i] - 1)
print(ans)
