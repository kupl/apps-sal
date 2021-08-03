n, m = map(int, input().split())
c = list(map(int, input().split()))
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

vs = [False for i in range(n)]
ans = 0
for i in range(n):
    if vs[i]:
        continue
    q = [i]
    vs[i] = True
    m = c[i]
    while len(q) > 0:
        v = q[0]
        del q[0]
        for u in g[v]:
            if not vs[u]:
                vs[u] = True
                q.append(u)
                m = min(m, c[u])
    ans += m

print(ans)
