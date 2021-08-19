from sys import stdin


def main():
    # 入力
    readline = stdin.readline
    s = readline().strip()

    mod = 10**9 + 7
    n = len(s)
    dp = [[0] * 4 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        # i文字目を選ばない
        for j in range(4):
            if s[i - 1] != "?":
                dp[i][j] += dp[i - 1][j]
            else:
                dp[i][j] += dp[i - 1][j] * 3

        # i文字目を選ぶ
        if s[i - 1] == "A":
            dp[i][1] += dp[i - 1][0]
        elif s[i - 1] == "B":
            dp[i][2] += dp[i - 1][1]
        elif s[i - 1] == "C":
            dp[i][3] += dp[i - 1][2]
        elif s[i - 1] == "?":
            dp[i][1] += dp[i - 1][0]
            dp[i][2] += dp[i - 1][1]
            dp[i][3] += dp[i - 1][2]

        for j in range(4):
            dp[i][j] %= mod

    print(dp[n][3])


def __starting_point():
    main()


__starting_point()
