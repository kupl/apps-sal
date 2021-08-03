def main():
    INF = 100 * 40 + 1
    MX = 4000

    N, Ma, Mb = list(map(int, input().split()))

    dp = [[INF] * (MX * 2 + 1) for _ in range(2)]
    i, j = 0, 1
    for _ in range(N):
        ai, bi, ci = list(map(int, input().split()))
        x = Ma * bi - Mb * ai  # Σai:Σbi=Ma:Mb<->Ma*Σbi-Mb*Σai=0

        for k in range(-MX, MX + 1):
            dp[j][k] = dp[i][k]
        dp[j][x] = min(dp[j][x], ci)

        for k in range(-MX + x, MX + 1):
            dp[j][k] = min(
                dp[j][k],
                dp[i][k - x] + ci
            )
        i, j = j, i

    res = dp[i][0]
    print((-1 if res == INF else res))


def __starting_point():
    main()


__starting_point()
