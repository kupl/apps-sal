import sys
sys.setrecursionlimit(10**8)
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)


def dfs(v):
    if len(edge[v]) == 0:
        return 0
    for u in edge[v]:
        if visited[u] == False:
            visited[u] = True
            dfs(u)
    return 0


ans = 0
visited = [False] * N
for i in range(N):
    if visited[i] == False:
        visited[i] = True
        dfs(i)
        ans += 1
print(ans)
