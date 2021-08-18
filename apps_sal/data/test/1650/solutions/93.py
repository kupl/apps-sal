def main():
    MOD = 10 ** 9 + 7

    EQ = 0
    SMALL = 1

    S = list(map(int, input()))
    dp = [1, 0]
    for x in S:
        ndp = [0] * 2

        if x == 0:
            ndp[EQ] = dp[EQ]
            ndp[SMALL] = dp[SMALL] * 3
        elif x == 1:
            ndp[EQ] = dp[EQ] * 2
            ndp[SMALL] = dp[EQ] + dp[SMALL] * 3

        *dp, = [x % MOD for x in ndp]

    ans = sum(dp) % MOD

    print(ans)


def __starting_point():
    main()


__starting_point()
