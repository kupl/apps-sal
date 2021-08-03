import sys
sys.setrecursionlimit(10**8)
N = int(input())
graph = [[] for _ in range(N)]

for i in range(1, N):
    u, v, w = list(map(int, input().split()))
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

color = [0 for _ in range(N)]
visited = [False for _ in range(N)]


def dfs(now):

    for adj in graph[now]:
        v, dist = adj
        if visited[v]:
            continue
        visited[v] = True
        color[v] = color[now] + dist
        dfs(v)

    return


for start in range(N):
    if not visited[start]:
        color[start] = 0
        visited[start] = True
        dfs(start)

for i in range(N):
    print((color[i] % 2))
