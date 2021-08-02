def main():
    N = input()
    L = len(N)
    K = int(input())
    dp = [[0 for _ in range(L + 1)] for _ in range(K + 1)]
    dpp = [[0 for _ in range(L + 1)] for _ in range(K + 1)]
    dpp[0][0] = 1
    for i in range(1, L + 1):
        n = int(N[i - 1])
        for k in range(K + 1):
            # from dpp
            kk = k + (1 if n > 0 else 0)
            if kk <= K:
                dpp[kk][i] = dpp[k][i - 1]
            if n > 0:
                dp[k][i] += dpp[k][i - 1]
                if k + 1 <= K:
                    dp[k + 1][i] += (n - 1) * dpp[k][i - 1]
            # from dp
            dp[k][i] += dp[k][i - 1]
            if k + 1 <= K:
                dp[k + 1][i] += 9 * dp[k][i - 1]
    print(dp[K][L] + dpp[K][L])


def __starting_point():
    main()


__starting_point()
