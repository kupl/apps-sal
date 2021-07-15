import sys
sys.setrecursionlimit(200000)

N, s, t = map(int, input().split())
s -= 1; t -= 1
to = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    to[a].append(b)
    to[b].append(a)

def calcDist(u):
    dfs(u)
    return dist

def dfs(v, d=0, p=-1):
    dist[v] = d
    for u in to[v]:
        if u == p:
            continue
        dfs(u, d+1, v)

dist = [0 for _ in range(N)]
distS = calcDist(s)
dist = [0 for _ in range(N)]
distT = calcDist(t)

ans = 0
for i in range(N):
    if distS[i] < distT[i]:
        ans = max(ans, distT[i])

print(ans-1)
