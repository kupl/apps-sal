N, M = map(int, input().split())
graph = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(x, g):
    if vis[x]:
        return
    vis[x] = 1
    for i in g[x]:
        dfs(i, g)
    return


ans = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        t = graph[i]
        gn = graph[0:i] + [t[0:j] + t[j + 1:]] + graph[i + 1:]
        vis = [0] * N
        dfs(0, gn)
        if not(all(vis)):
            ans += 1
print(ans)
