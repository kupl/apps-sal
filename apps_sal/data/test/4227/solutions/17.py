def dfs(g, v, depth):
    if seen[v] == True:
        return 0
    if depth == n:
        return 1
    seen[v] = True
    paths = 0
    for next_v in g[v]:
        paths += dfs(g, next_v, depth + 1)
    seen[v] = False
    return paths


(n, m) = map(int, input().split())
g = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    (a, b) = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
seen = [False] * (n + 1)
print(dfs(g, 1, 1))
