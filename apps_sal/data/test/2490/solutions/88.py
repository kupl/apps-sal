def main():
    s = input()
    dp = [0, 1]
    for c in s:
        x = int(c)
        a = dp[0] + x
        if a > dp[1] + 10 - x:
            a = dp[1] + 10 - x
        b = dp[0] + x + 1
        if b > dp[1] + 10 - x - 1:
            b = dp[1] + 10 - x - 1
        dp[0] = a
        dp[1] = b
    dp[1] += 1
    print((min(dp)))


def __starting_point():
    main()


__starting_point()
