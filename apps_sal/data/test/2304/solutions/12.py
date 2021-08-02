from collections import deque
n, m = list(map(int, input().split()))
g = [[] for _ in range(n + 1)]
q = deque([])
visited = set()
dist = [None] * (n + 1)

for i in range(m):
    a, b, k = list(map(int, input().split()))
    g[a].append((b, k))
    g[b].append((a, -k))


def dfs(u):
    q.append(u)
    while q:
        v = q.pop()
        visited.add(v)
        for x, d in g[v]:
            if x not in visited:
                if dist[x] is None:
                    dist[x] = dist[v] + d
                elif dist[x] != dist[v] + d:
                    return False
                q.append(x)
    return True


for i in range(1, n + 1):
    if i not in visited:
        dist[i] = 1
        if not dfs(i):
            print("No")
            return
print("Yes")
