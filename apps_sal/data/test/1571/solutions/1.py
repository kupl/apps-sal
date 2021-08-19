import sys
readline = sys.stdin.readline
S = input()
T = '*' + input()
(n, m) = (len(S), len(T))
mod = 998244353
dp = [[0] * (n + 5) for _ in range(n + 5)]
for i in range(n + 1):
    dp[i][i + 1] = 1
for (i, c) in enumerate(S, start=1):
    for (l, r) in zip(list(range(0, n + 1)), list(range(i, n + 2))):
        if l >= m or (0 < l and T[l] == c):
            dp[l - 1][r] += dp[l][r] % mod
        if r >= m or T[r] == c:
            dp[l][r + 1] += dp[l][r] % mod
print(sum(dp[0][m:]) % mod)
