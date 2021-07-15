def bfs(s):
    d = [0] * n
    vs = {s}
    nr = {s}
    while len(vs) < n:
        cr = nr
        nr = set()
        for u in cr:
            for v in g[u] - vs:
                vs.add(v)
                d[v] = d[u] + 1
                nr.add(v)
    return d


n, m, s, t = list(map(int, input().split()))
s -= 1
t -= 1

g = [set() for _ in range(n)]
for i in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    g[u].add(v)
    g[v].add(u)

ds = bfs(s)
dt = bfs(t)
mindist = ds[t]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if min(ds[i] + dt[j], ds[j] + dt[i]) >= mindist - 1:
            ans += 1

print(ans - m)

