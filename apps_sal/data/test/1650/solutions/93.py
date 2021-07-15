def main():
    MOD = 10 ** 9 + 7

    EQ = 0  # 等しくなり得る
    SMALL = 1  # 未満確定

    S = list(map(int, input()))
    dp = [1, 0]
    for x in S:
        ndp = [0] * 2

        if x == 0:
            ndp[EQ] = dp[EQ]  # (0,0)
            ndp[SMALL] = dp[SMALL] * 3  # (0,0),(0,1),(1,0)
        elif x == 1:
            ndp[EQ] = dp[EQ] * 2  # (0,1),(1,0)
            ndp[SMALL] = dp[EQ] + dp[SMALL] * 3  # EQ->(0,0), SMALL->(0,0),(0,1),(1,0)

        *dp, = [x % MOD for x in ndp]

    ans = sum(dp) % MOD  # 取り忘れ

    print(ans)


def __starting_point():
    main()

__starting_point()
