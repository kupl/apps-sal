N, Ma, Mb = list(map(int, input().split()))
dp = [{} for i in range(N + 1)]
dp[0][(0, 0)] = 0
for i in range(N):
    a, b, c = list(map(int, input().split()))
    for p, q in dp[i]:
        if (p, q) not in dp[i + 1]:
            dp[i + 1][(p, q)] = 100000
        dp[i + 1][(p, q)] = min(dp[i + 1][(p, q)], dp[i][(p, q)])
        if (p + a, q + b) not in dp[i + 1]:
            dp[i + 1][(p + a, q + b)] = 100000
        dp[i + 1][(p + a, q + b)] = min(dp[i + 1][(p + a, q + b)], dp[i][(p, q)] + c)
rs = []
for k in range(1, 10000):
    if (k * Ma, k * Mb) in dp[N]:
        r = dp[N][(k * Ma, k * Mb)]
        rs.append(r)
if len(rs) == 0:
    print((-1))
else:
    r = min(rs)
    print(r)
