import collections

n, m, p = list(map(int, input().split()))
dist1 = []
edges1 = [[] for _ in range(n)]
edges2 = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    dist1.append((a, b, (c - p) * -1))
    edges1[a].append(b)
    edges2[b].append(a)

def dfs(edges, start):
    stack = [start]
    use = {start, }
    while stack:
        x = stack.pop()
        for y in edges[x]:
            if y in use:
                continue
            stack.append(y)
            use.add(y)
    return use


def bellman_ford(dist):
    v = [float('inf')] * n
    v[0] = 0
    for _ in range(n):
        updated = False
        for a, b, c in dist:
            if v[a] + c < v[b]:
                updated = True
                v[b] = v[a] + c
        if not updated:
            return max(0, v[n - 1] * -1)
    return -1

use = dfs(edges1, 0) & dfs(edges2, n - 1)
dist2 = [(a, b, c) for a, b, c in dist1 if a in use and b in use]
print((bellman_ford(dist2)))

