mod = 998244353
(N, S, *A) = map(int, open(0).read().split())
dp = [1] + [0] * S
for (i, a) in enumerate(A, 1):
    dp = [(2 * dp[j] + (dp[j - a] if j >= a else 0)) % mod for j in range(S + 1)]
print(dp[S])
