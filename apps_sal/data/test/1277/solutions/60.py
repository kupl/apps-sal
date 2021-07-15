import sys
sys.setrecursionlimit(1000000000)

n,u,v = map(int,input().split())
u -= 1
v -= 1
G = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

distT = [-1]*n
distA = [-1]*n
distT[u] = 0
distA[v] = 0
def dfs(now,dist):
    for nxt in G[now]:
        if dist[nxt] != -1: continue
        dist[nxt] = dist[now]+1
        dfs(nxt,dist)
dfs(u,distT)
dfs(v,distA)

mx = 0
for i in range(n):
    if distT[i] < distA[i]:
        mx = max(mx, distA[i])
ans = mx-1
print(ans)
