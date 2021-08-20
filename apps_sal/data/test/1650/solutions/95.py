def main():
    MOD = 10 ** 9 + 7
    L = input()
    N = len(L)
    dp = [0 for _ in range(N + 1)]
    dpp = [0 for _ in range(N + 1)]
    dpp[0] = 1
    for n in range(1, N + 1):
        dpp_v = dpp[n - 1]
        d = int(L[n - 1])
        dpp[n] = (d + 1) * dpp_v % MOD
        dp[n] = (3 * dp[n - 1] + d * dpp_v) % MOD
    print((dp[N] + dpp[N]) % MOD)


def __starting_point():
    main()


__starting_point()
