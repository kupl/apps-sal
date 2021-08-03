n, k = map(int, input().split())
l = []
r = []
MOD = 998244353
for i in range(k):
    i1, i2 = map(int, input().split())
    l.append(i1)
    r.append(i2)

dp = [0] * (n + 1)
dpsum = [0] * (n + 1)
dp[1] = 1
dpsum[1] = 1

for i in range(1, n + 1):
    for j in range(k):
        li = i - r[j]
        ri = i - l[j]
        if ri < 0:
            continue
        li = max(0, li)
        dp[i] += (dpsum[ri] - dpsum[li - 1]) % MOD
    dpsum[i] = (dpsum[i - 1] + dp[i]) % MOD

print(dp[n] % MOD)
