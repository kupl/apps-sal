def dfs(v):
    used[v] = 1
    for i in graph[v]:
        if not used[i]:
            dfs(i)

n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1] += [b - 1]
    graph[b - 1] += [a - 1]
used = [0 for i in range(n)]

counter = 0
for i in range(n):
    if not used[i]:
        dfs(i)
        counter += 1
print(2 ** (n - counter))
