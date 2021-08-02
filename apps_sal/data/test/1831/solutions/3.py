def read(): return list(map(int, input().split()))


n, m = read()
g = [list() for i in range(n + 1)]
for i in range(m):
    a, b = read()
    g[a].append(b)
    g[b].append(a)


def dfs(v):
    was[v] = 1
    for u in g[v]:
        if not was[u]:
            dfs(u)


was = [0] * (n + 1)
dfs(1)
ans = 'no' if 0 in was[1:] or m != n - 1 else 'yes'
print(ans)
