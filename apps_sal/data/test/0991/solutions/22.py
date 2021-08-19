from heapq import heappop, heappush
(n, m, s) = list(map(int, input().split()))
uvab = [list(map(int, input().split())) for _ in range(m)]
cd = [list(map(int, input().split())) for _ in range(n)]
g = [[] for _ in range(n)]
maxs = 0
for (u, v, a, b) in uvab:
    (u, v) = (u - 1, v - 1)
    g[u].append([v, a, b])
    g[v].append([u, a, b])
    maxs += a
inf = float('inf')
ans = [[inf] * (maxs + 1) for _ in range(n)]
s = min(s, maxs)
todo = [[0, 0, s]]
ans[0][s] = 0
while todo:
    (t, v, ss) = heappop(todo)
    if ans[v][ss] < t:
        continue
    for (nv, na, nb) in g[v]:
        if na > ss:
            continue
        if ans[nv][ss - na] > t + nb:
            heappush(todo, [t + nb, nv, ss - na])
            ans[nv][ss - na] = t + nb
    (c, d) = cd[v]
    nss = min(ss + c, maxs)
    if ans[v][nss] > t + d:
        heappush(todo, [t + d, v, nss])
        ans[v][nss] = t + d
for i in range(1, n):
    print(min(ans[i]))
