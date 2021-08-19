import sys
(n, m, s) = list(map(int, input().split()))
adj = [[] for _ in range(500005)]
ar = []
vis = [0] * 500005
sys.setrecursionlimit(6000)


def dfs(s):
    vis[s] = 1
    for i in range(len(adj[s])):
        if vis[adj[s][i]] == 0:
            dfs(adj[s][i])
    ar.append(s)


for i in range(m):
    (u, v) = list(map(int, input().split()))
    adj[u].append(v)
dfs(s)
for i in range(n):
    if vis[i + 1] == 0:
        dfs(i + 1)
res = 0
vis = [0] * 500005
for i in range(n - 1, -1, -1):
    if vis[ar[i]] == 0:
        if s != ar[i]:
            res += 1
        dfs(ar[i])
print(res)
