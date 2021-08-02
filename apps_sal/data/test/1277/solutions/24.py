import sys
sys.setrecursionlimit(10**7)

n, u, v = map(int, input().split())
u -= 1
v -= 1

graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


dist = [[-1, -1] for _ in range(n)]
dist[v][0] = 0
dist[u][1] = 0


def dfs(graph, v, k):
    ver = graph[v]
    for vers in ver:
        if dist[vers][k] == -1:
            dist[vers][k] = dist[v][k] + 1
            dfs(graph, vers, k)


dfs(graph, v, 0)
dfs(graph, u, 1)
dist.sort(reverse=True)

for i in range(10**6):
    if dist[i][0] - dist[i][1] >= 1:
        print(dist[i][0] - 1)
        break
