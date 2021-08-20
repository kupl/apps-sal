def dj(s, dist, g):
    dist[x] = 0
    q = [s]
    while q:
        c = q.pop()
        for to in g[c]:
            if not dist[to]:
                dist[to] = dist[c] + 1
                q.insert(0, to)
    dist[s] = 0


(n, m, s, f) = [int(x) for x in input().split()]
s = s - 1
f = f - 1
g = [[] for i in range(n)]
for i in range(m):
    (x, y) = [int(x) for x in input().split()]
    x = x - 1
    y = y - 1
    g[x].append(y)
    g[y].append(x)
INF = int(1000000000.0)
dist_s = [0 for i in range(n)]
dist_f = [0 for i in range(n)]
dj(s, dist_s, g)
dj(f, dist_f, g)
res = 0
for i in range(n):
    for j in range(i + 1, n):
        if dist_s[i] + dist_f[j] + 1 >= dist_s[f] and dist_f[i] + dist_s[j] + 1 >= dist_s[f] and (j not in g[i]):
            res = res + 1
print(res)
