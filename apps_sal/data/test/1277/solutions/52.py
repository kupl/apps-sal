import sys
sys.setrecursionlimit(10**6)

n, u, v = map(int, input().split())
u, v = u - 1, v - 1
edges = [[] for i in range(n)]
for i in range(n - 1):
    ai, bi = map(int, input().split())
    ai, bi = ai - 1, bi - 1
    edges[ai].append(bi)
    edges[bi].append(ai)


def dfs(already, node, depth):
    depth += 1
    children = edges[node]
    for child in children:
        if already[child] == 0:
            already[child] = depth
            already = dfs(already, child, depth)
    return already


already_u = [0 for i in range(n)]
already_u[u] = -1
already_u = dfs(already_u, u, 0)
already_u[u] = 0
already_v = [0 for i in range(n)]
already_v[v] = -1
already_v = dfs(already_v, v, 0)
already_v[v] = 0

maxi = 0
for i in range(n):
    if already_u[i] < already_v[i]:
        maxi = max(maxi, already_v[i])
print(maxi - 1)
