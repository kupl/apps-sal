def read(): return list(map(int, input().split()))


n, m = read()
g = [list() for i in range(n + 1)]
f = [0] * (n + 1)
ans = 0
for i in range(m):
    u, v = read()
    g[v].append(u)
    g[u].append(v)
for i in range(1, n + 1):
    if f[i]:
        continue
    ch = [(i, 0)]
    f[i] = flag = 1
    while ch:
        v, p = ch.pop()
        for u in g[v]:
            if u == p:
                continue
            if f[u] == 1:
                flag = 0
            if f[u] == 0:
                ch.append((u, v))
                f[u] = 1
    ans += flag
print(ans)
