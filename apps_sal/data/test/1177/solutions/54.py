def main():
    MOD = 998244353
    (N, S) = list(map(int, input().split()))
    (*A,) = list(map(int, input().split()))
    ans = 0
    dp = [0] * (S + 1)
    for (i, a) in enumerate(A, start=1):
        dp[0] = i
        ans += dp[S]
        if S >= a:
            ans += dp[S - a]
        ans %= MOD
        for s in reversed(list(range(a, S + 1))):
            dp[s] += dp[s - a]
            dp[s] %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
