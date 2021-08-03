N, M = list(map(int, input().split()))


def dfs(node):
    if sum([1 for v in visited if v]) == N:
        return 1
    ret = 0
    for n in graph[node]:
        if visited[n]:
            continue
        visited[n] = True
        ret += dfs(n)
        visited[n] = False
    return ret


graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

visited = [False for _ in range(N)]
visited[0] = True
print((dfs(0)))
