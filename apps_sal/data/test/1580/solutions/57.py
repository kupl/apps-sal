import sys
sys.setrecursionlimit(10**9)

N, M = list(map(int, input().split()))
paths = [[] for _ in range(N)]

for _ in range(M):
    a, b, z = list(map(int, input().split()))
    paths[a - 1].append(b - 1)
    paths[b - 1].append(a - 1)

visited = [False] * N


def dfs(node, prev):
    if visited[node]:
        return
    visited[node] = True
    for n in paths[node]:
        if n != prev:
            dfs(n, node)


count = 0
for i in range(N):
    if visited[i] == False:
        count += 1
        dfs(i, -1)

print(count)
