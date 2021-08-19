import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 8)
N = int(input())
graph = [[] for _ in range(N)]
numOfEdges = [0 for _ in range(N)]
visited = [0 for _ in range(N)]
edges = defaultdict(int)
for i in range(1, N):
    (a, b) = list(map(int, input().split()))
    a -= 1
    b -= 1
    numOfEdges[a] += 1
    numOfEdges[b] += 1
    edges[a, b] = 0
    graph[a].append(b)
    graph[b].append(a)


def dfs(prev, now, col):
    if visited[now]:
        return
    visited[now] = 1
    i = 1
    for adj in graph[now]:
        if adj == prev:
            continue
        if now < adj:
            edges[now, adj] = col + i
        else:
            edges[adj, now] = col + i
        dfs(now, adj, col + i)
        i += 1


dfs(-1, 0, 1)
maxColor = max(numOfEdges)
print(maxColor)
for (k, i) in list(edges.items()):
    e = i % maxColor
    if e:
        print(e)
    else:
        print(maxColor)
