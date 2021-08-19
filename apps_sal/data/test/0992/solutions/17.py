(N, S) = list(map(int, input().split()))
A = list(map(int, input().split()))


def f(N, S, A):
    MOD = 998244353
    dp = [0] * (S + 1)
    dp[0] = pow(2, N, MOD)
    div = pow(2, MOD - 2, MOD)
    m = 0
    for a in A:
        m += a
        for i in range(min(m, S), a - 1, -1):
            dp[i] = (dp[i] + dp[i - a] * div) % MOD
    return dp[S]


print(f(N, S, A))
