import sys
sys.setrecursionlimit(10**5+1)

N, M = map(int, input().split())

edge = [[] for i in range(N)]
for i in range(M):
    x, y, _ = map(int, input().split())
    edge[x-1].append(y-1)
    edge[y-1].append(x-1)

visited = [False] * N

ans = 0
def dfs(x):
    nonlocal ans
    if not visited[x]:
        ans += 1
    visited[x] = True

    for x_next in edge[x]:
        if visited[x_next]:
           continue 
        visited[x_next] = True
        dfs(x_next)

for i in range(N):
    dfs(i)

print(ans)
