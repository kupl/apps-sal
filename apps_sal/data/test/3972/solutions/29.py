MOD = 10 ** 9 + 7
n = int(input())
if n == 1:
    print(1)
else:
    dp = [0 for _ in range(n + 1)]
    (dp[0], dp[1], dp[2]) = (1, 1, 1)
    cum = [0 for _ in range(n + 1)]
    (cum[0], cum[1], cum[2]) = (1, 2, 3)
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + cum[i - 3]) % MOD
        cum[i] = (cum[i - 1] + dp[i]) % MOD
    ans = cum[n - 2] * (n - 1) * (n - 1) + dp[n - 1] * (n - 1) + cum[n - 2] * (n - 1) + 1
    print(ans % MOD)
