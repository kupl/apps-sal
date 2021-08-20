(n, m) = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    (u, v) = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
dp = [1 for _ in range(n)]
for i in range(n):
    for v in graph[i]:
        if v < i:
            dp[i] = max(dp[i], dp[v] + 1)
print(max([dp[i] * len(graph[i]) for i in range(n)]))
