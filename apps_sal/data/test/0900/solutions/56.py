def main():
    S = input().rstrip()
    ans, MOD = [0] * 13, 10 ** 9 + 7
    ans[0] = 1
    for c in S:
        dp = [0] * 13
        for i in range(13):
            dp[(i * 10) % 13] = ans[i] % MOD
        dp += dp
        if c == "?":
            for i in range(13):
                ans[i] = sum(dp[i + 4: i + 14])
        else:
            x = int(c)
            for i in range(13):
                ans[i] = dp[i + 13 - x]
    print(ans[5] % MOD)


def __starting_point():
    main()


__starting_point()
