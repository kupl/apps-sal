def dfs(start, path):
    res = 0
    path.append(start)
    if len(path) == N:
        res += 1
        return res
    for i in graph[start]:
        if i not in path:
            res += dfs(i, path)
            path.pop()
    return res


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
print(dfs(0, []))
