def main():
    MOD = 998244353
    (N, S) = list(map(int, input().split()))
    (*A,) = list(map(int, input().split()))
    dp = [0] * (S + 1)
    ans = 0
    for x in A:
        ans += dp[S]
        if S >= x:
            ans += dp[S - x]
            if S == x:
                ans += 1
            for s in range(S, x, -1):
                dp[s] = (dp[s] + dp[s - x]) % MOD
            dp[x] = (dp[x] + dp[0] + 1) % MOD
        dp[0] += 1
        ans %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
