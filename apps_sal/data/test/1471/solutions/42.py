from sys import setrecursionlimit
setrecursionlimit(10 ** 7)
n = int(input())
uvw = [list(map(int, input().split())) for i in range(n - 1)]
d = [-1 for i in range(n)]
edge = [[] for i in range(n)]
for u, v, w in uvw:
    edge[u - 1].append((v - 1, w))
    edge[v - 1].append((u - 1, w))


def dfs(now, D):
    d[now] = D
    for i, j in edge[now]:
        if d[i] == -1:
            dfs(i, D + j)


dfs(0, 0)
for i in d:
    print(i % 2)
