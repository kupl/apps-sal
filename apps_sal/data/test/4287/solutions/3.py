rd = lambda: list(map(int, input().split()))
a, n, m = rd()
s = set()
u = {}
k = set([0, a])
for _ in range(n):
    l, r = rd()
    for x in range(l + 1, r + 1):
        s.add(x)
    k.add(r)
for _ in range(m):
    x, p = rd()
    u[x] = min(p, u.get(x, 1e9))
    k.add(x)
k = sorted(list(k))
dp = {}
dp[0] = {}
dp[0][0] = 0
if 0 in u:
    dp[0][u[0]] = 0
for i in range(1, len(k)):
    x = k[i]
    y = k[i - 1]
    dp[x] = {}
    for z in dp[y]:
        if z:
            dp[x][z] = dp[y][z] + z * (x - y)
        else:
            if x not in s:
                dp[x][0] = dp[y][0]
    if len(dp[x]):
        dp[x][0] = min(dp[x].values())
        if x in u:
            if u[x] not in dp[x] or dp[x][0] < dp[x][u[x]]:
                dp[x][u[x]] = dp[x][0]
    else:
        print(-1)
        return
print(dp[a][0])

