def main():
    MOD = 10 ** 9 + 7
    S = input()
    N = len(S)
    CHARS = ['A', 'B', 'C']
    dp = [[0 for _ in range(4)] for _ in range(N + 1)]
    dp[N][3] = 1
    for i in range(N - 1, -1, -1):
        a = 3 if S[i] == '?' else 1
        dp[i][3] = a * dp[i + 1][3]
        dp[i][3] %= MOD
    for i in range(N - 1, -1, -1):
        a = 3 if S[i] == '?' else 1
        ch = S[i]
        for j in range(3):
            b = 1 if ch in ['?', CHARS[j]] else 0
            dp[i][j] = a * dp[i + 1][j] + b * dp[i + 1][j + 1]
            dp[i][j] %= MOD
    print(dp[0][0])


def __starting_point():
    main()


__starting_point()
