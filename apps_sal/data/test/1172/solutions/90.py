def main():
    S = input()
    N = len(S)
    m = 10 ** 9 + 7
    dp = [[0] * 4 for _ in range(N + 1)]
    for i in range(N, -1, -1):
        for j in range(3, -1, -1):
            if i == N:
                if j == 3:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
            else:
                if S[i] == '?':
                    dp[i][j] = dp[i + 1][j] * 3 % m
                else:
                    dp[i][j] = dp[i + 1][j]
                if j < 3:
                    if S[i] == '?' or S[i] == 'ABC'[j]:
                        dp[i][j] += dp[i + 1][j + 1]
                        dp[i][j] %= m
    print(dp[0][0])


def __starting_point():
    main()


__starting_point()
