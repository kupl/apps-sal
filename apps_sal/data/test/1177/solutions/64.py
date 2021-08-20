def solve():
    MOD = 998244353
    (N, S) = list(map(int, input().split()))
    As = list(map(int, input().split()))
    ans = 0
    dp = [0] * (S + 1)
    dp[0] = 1
    for A in As:
        for sm in reversed(list(range(S - A + 1))):
            dp[sm + A] += dp[sm]
            dp[sm + A] %= MOD
        ans += dp[S]
        ans %= MOD
        dp[0] += 1
        dp[0] %= MOD
    print(ans)


solve()
