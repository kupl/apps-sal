def dfs(v):
    if sum(visited) == N:
        return 1
    res = 0
    for nv in g[v]:
        if visited[nv]:
            continue
        visited[nv] = 1
        res += dfs(nv)
        visited[nv] = 0
    return res


(N, M, *ab) = list(map(int, open(0).read().split()))
g = [[] for _ in range(N)]
for (a, b) in zip(*[iter(ab)] * 2):
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
visited = [0] * N
visited[0] = 1
print(dfs(0))
