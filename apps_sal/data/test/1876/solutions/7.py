n,k = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n-1):
    u,v,x = map(int, input().split())
    g[u-1].append((v-1, x))
    g[v - 1].append((u - 1, x))

v = [0 for i in range(n)]
comps = []
for i in range(n):
    if v[i] == 1:
        continue
    v[i] = 1
    comps.append([i])
    q = [i]
    while q:
        u0 = q[0]
        q = q[1:]
        for u, x in g[u0]:
            if x == 0 and v[u] == 0:
                q.append(u)
                v[u] = 1
                comps[-1].append(u)

ans = n**k

for comp in comps:
    ans -= len(comp)**k
print(ans%((10**9) + 7))
