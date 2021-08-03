import sys
sys.setrecursionlimit(10 ** 6)
N, u, v = map(int, input().split())
u -= 1
v -= 1
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

dist = [0] * N


def dfs(v, d=0, p=-1):
    nonlocal dist
    dist[v] = d
    for u in edges[v]:
        if u == p:
            continue
        dfs(u, d + 1, v)


def calc_dist(s):
    nonlocal dist
    dist = [0] * N
    dfs(s)
    return dist


distS = calc_dist(u)
distT = calc_dist(v)

mx = 0
for i in range(N):
    if distS[i] < distT[i]:
        mx = max(mx, distT[i])
ans = mx - 1
print(ans)
