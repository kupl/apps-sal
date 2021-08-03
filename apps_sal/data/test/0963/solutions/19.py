n, k = map(int, input().split())
mod = 998244353
l, r = [0] * n, [0] * n
dp = [0] * (n + 1)
ans = [0] * n
ans[0] = 1
dp[1] = 1
for i in range(k):
    l[i], r[i] = map(int, input().split())


for i in range(1, n):
    total = 0
    for j in range(k):
        total += dp[i - l[j] + 1] - dp[i - r[j]]
    ans[i] = total % mod
    dp[i + 1] = dp[i] + ans[i]
print(ans[-1])
