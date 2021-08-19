(n, k) = [int(i) for i in input().split()]
rng = [[int(i) for i in input().split()] for i in range(k)]
mod = 998244353
dp = [0] * n
dp[0] = 1
dp_acc = [0, 1]
for i in range(1, n):
    for (l, r) in rng:
        dp[i] += dp_acc[max(0, i - l + 1)] - dp_acc[max(0, i - r)]
        dp[i] %= mod
    dp_acc.append(dp_acc[i] + dp[i])
print(dp[n - 1])
