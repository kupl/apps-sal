import sys
sys.setrecursionlimit(10**7)


n, u, v = list(map(int, input().split()))
u -= 1
v -= 1

graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

# ab=[list(map(int, input().split())) for _ in range(n-1)]
# for a,b in ab:
#     graph[a-1].append(b-1)
#     graph[b-1].append(a-1)

dist = [[-1, -1] for _ in range(n)]
dist[v][0] = 0
dist[u][1] = 0


def dfs1(graph, v):
    vv = graph[v]
    for vvv in vv:
        if dist[vvv][0] == -1:
            dist[vvv][0] = dist[v][0] + 1
            dfs1(graph, vvv)


def dfs2(graph, v):
    vv = graph[v]
    for vvv in vv:
        if dist[vvv][1] == -1:
            dist[vvv][1] = dist[v][1] + 1
            dfs2(graph, vvv)


dfs1(graph, v)
dfs2(graph, u)
dist.sort(reverse=True)

for i in range(10**6):
    if dist[i][0] - dist[i][1] >= 1:
        print((dist[i][0] - 1))
        break
