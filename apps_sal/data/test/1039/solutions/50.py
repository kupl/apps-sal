import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
edge = [[] for i in range(n)]
for i in range(n - 1):
    (x, y, z) = map(int, input().split())
    edge[x - 1].append([y - 1, z])
    edge[y - 1].append([x - 1, z])
(q, k) = map(int, input().split())
dist = [-1] * n


def dfs(node, d):
    dist[node] = d
    for i in edge[node]:
        if dist[i[0]] == -1:
            dfs(i[0], d + i[1])


dfs(k - 1, 0)
for i in range(q):
    (x, y) = map(int, input().split())
    print(dist[x - 1] + dist[y - 1])
