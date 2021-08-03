import sys
sys.setrecursionlimit(1 << 30)


def dfs(x):
    for y in edges[x]:
        if y != parent[x]:
            parent[y] = x
            count[y] += count[x]
            dfs(y)


N, Q = map(int, input().split())
edges = [[] for _ in range(N + 1)]
count = [0] * (N + 1)
for i in range(N - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
for i in range(Q):
    p, x = map(int, input().split())
    count[p] += x

parent = [-1] * (N + 1)
dfs(1)
print(*count[1:])
