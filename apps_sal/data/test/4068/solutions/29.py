def main3():
    (N, M) = map(int, input().split())
    ng_step = set([int(input()) for _ in range(M)])
    dp = [0 for i in range(N + 1)]
    dp[0] = 1
    if 1 in ng_step:
        dp[1] = 0
    else:
        dp[1] = 1
    for i in range(2, N + 1):
        if i in ng_step:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[N] % (10 ** 9 + 7))


def __starting_point():
    main3()


__starting_point()
