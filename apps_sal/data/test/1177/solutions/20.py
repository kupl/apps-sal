mod = 998244353
(N, S, *A) = map(int, open(0).read().split())
dp = [0] * (S + 1)
ans = 0
for (i, a) in enumerate(A, 1):
    if a <= S:
        T = dp[:]
        for j in range(a, S + 1):
            dp[j] += T[j - a]
        dp[a] += i
    ans += dp[-1]
    ans %= mod
print(ans)
