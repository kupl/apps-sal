def solve():
    MOD = 10**9 + 7

    N, M = list(map(int, input().split()))
    Ss = list(map(int, input().split()))
    Ts = list(map(int, input().split()))

    dp = [1]*(M+1)
    for i, S in enumerate(Ss, 1):
        dp2 = [1]*(M+1)
        for j, T in enumerate(Ts, 1):
            dp2[j] = dp[j] + dp2[j-1]
            if S != T:
                dp2[j] -= dp[j-1]
            dp2[j] %= MOD
        dp = dp2

    print((dp[-1]))


solve()

