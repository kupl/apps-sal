n,m = list(map(int, input().split()))
p = list(map(int, input().split()))
p.insert(0, 0)

vis = [0] * (n+7)
G = [[0] for i in range(n+7)]
for i in range(m):
    u, v = list(map(int, input().split()))
    G[v].append(u)

for x in G[p[n]]:
    vis[x] += 1

ans = 0
cnt = 1
for i in range(n - 1, 0, -1):
    now = p[i]
    if vis[now] == cnt:
        ans += 1
    else:
        cnt += 1
        for y in G[now]:
            vis[y] += 1

print(ans)
    

