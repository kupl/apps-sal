def main():
    s = input().rstrip()
    s = "0" + s
    dp = [0, float("inf")]
    for c in s:
        x = int(c)
        dp = [min(dp[0] + x, dp[1] + (10 - x)), min(dp[0] + x + 1, dp[1] + (10 - x) - 1)]
    print((dp[0]))


def __starting_point():
    main()


__starting_point()
