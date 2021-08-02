inf = 10 ** 18

a = []
b = []
c = []
n, ma, mb = list(map(int, input().split()))

for _ in range(n):
    a_, b_, c_ = list(map(int, input().split()))
    a.append(a_)
    b.append(b_)
    c.append(c_)

abmax = 10
p = n * abmax
dp = [[[inf for _ in range(p + 1)] for _ in range(p + 1)]
      for _ in range(n + 1)]
dp[0][0][0] = 0

for i in range(n):
    for j in range(p + 1):
        for k in range(p + 1):
            if dp[i][j][k] == inf:
                continue
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            dp[i + 1][j + a[i]][k + b[i]
                                ] = min(dp[i + 1][j + a[i]][k + b[i]], dp[i][j][k] + c[i])

ans = inf
for j in range(p)[1::]:
    for k in range(p)[1::]:
        if j * mb == k * ma:
            ans = min(ans, dp[n][j][k])

if ans == inf:
    ans = -1
print(ans)
