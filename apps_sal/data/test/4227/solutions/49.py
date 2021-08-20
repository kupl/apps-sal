def dfs(now_node, depth):
    if seen[now_node]:
        return 0
    if depth == N:
        return 1
    seen[now_node] = True
    connect_nodes = graph[now_node]
    ans = 0
    for node in connect_nodes:
        ans += dfs(node, depth + 1)
    seen[now_node] = False
    return ans


(N, M) = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]
graph = [[] for i in range(N + 1)]
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
seen = [False for i in range(N + 1)]
seen[0] = True
print(dfs(1, 1))
