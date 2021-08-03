n, m = list(map(int, input().split()))
g = [[] for i in range(n)]
dg = [0 for i in range(n)]
for i in range(m):
    u, v = list(map(int, input().split()))
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)
    dg[u - 1] += 1
    dg[v - 1] += 1
vis = [0 for i in range(n)]
ans = 0
for i in range(n):
    if vis[i] != 0:
        continue
    q = [i]
    if dg[i] == 2:
        ans1 = 1
    else:
        ans1 = 0
    while len(q) > 0:
        v = q[0]
        for u in g[v]:
            if vis[u] == 0:
                vis[u] = 1
                q.append(u)
                if dg[u] != 2:
                    ans1 = 0
        del q[0]
    ans += ans1
print(ans)
