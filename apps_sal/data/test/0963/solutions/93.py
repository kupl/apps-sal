N, K = map(int, input().split())
mod = 998244353

LR = [list(map(int, input().split())) for _ in range(K)]

dp = [0] * (N + 1)
dp[1] = 1

memo = [0]
memo.append(1)
for i in range(2, N + 1):
    for l, r in LR:
        dp[i] += memo[max(0, i - l)] - memo[max(0, i - r - 1)]
        dp[i] %= mod
    memo.append(memo[-1] + dp[i])
print(dp[-1])
