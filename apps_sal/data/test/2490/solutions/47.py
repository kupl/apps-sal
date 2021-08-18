def main():
    *e, = list(map(int, input()))
    e.reverse()

    inf = 20 * len(e)

    dp = [0, inf]

    for x in e:
        ndp = [-1, -1]

        ndp[0] = min(
            dp[0] + x,
            dp[1] + ((x + 1) if x < 9 else inf)
        )

        ndp[1] = min(
            dp[0] + ((10 - x) if x > 0 else inf),
            dp[1] + (10 - (x + 1))
        )

        dp = ndp

    print((min(dp[0], dp[1] + 1)))


def __starting_point():
    main()


__starting_point()
