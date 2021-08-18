MOD = 998244353
N, K = list(map(int, input().split()))
kukan = [tuple(map(int, input().split())) for _ in range(K)]

dp = [0] * (N + 1)
dp[1] = 1

sumdp = [0] * (N + 1)
sumdp[1] = 1

for i in range(2, N + 1):
    for l, r in kukan:
        li = max(i - l, 0)
        ri = max(i - r - 1, 0)

        dp[i] += sumdp[li] - sumdp[ri]
        dp[i] %= MOD

    sumdp[i] = sumdp[i - 1] + dp[i]

print((dp[N]))
