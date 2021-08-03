from collections import defaultdict as d
from collections import deque


def bfs(adj, start, n):
    visited = [0] * (n + 1)
    tab = [0] * n
    q = deque([start])
    visited[start] = 1
    while q:
        s = q.popleft()
        for i in adj[s]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                tab[i - 1] = tab[s - 1] + 1
    return tab


n, u, v = map(int, input().split())
adj = d(list)
for i in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

takahashi = bfs(adj, u, n)
aoki = bfs(adj, v, n)
res = -1
for i in range(n):
    if takahashi[i] <= aoki[i]:
        res = max(res, aoki[i] - 1)

print(res)
