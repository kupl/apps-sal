import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    s = readline().rstrip().decode()
    n = len(s)
    # print(s)
    P = int(1e9) + 7
    dp = [[0, 0] for _ in range(n)]
    # dp[i][j]:=Lのi桁目まで見てLと一致する/未満である2数の組の数
    dp[0][0] = 1  # 未満となる組は(0, 0)の1通り
    dp[0][1] = 2  # 一致する組は(0, 1)と (1, 0)の2通り

    for i in range(1, n):
        if s[i] == '1':
            # dp[i-1][1]からの遷移は(0, 0)のみ。dp[i-1][0]からの遷移は(0, 0), (0, 1), (1, 0)
            dp[i][0] += dp[i - 1][1] + dp[i - 1][0] * 3
            # i桁目が1となる組は(1, 0)と(0, 1)の2通り
            dp[i][1] += dp[i - 1][1] * 2

            dp[i][0] %= P
            dp[i][1] %= P
        else:
            # (0, 0), (1, 0), (0, 1)を選ぶ
            dp[i][0] += dp[i - 1][0] * 3
            # (0, 0)を選ぶしかない
            dp[i][1] += dp[i - 1][1]

            dp[i][0] %= P
            dp[i][1] %= P

    print(((dp[n - 1][0] + dp[n - 1][1]) % P))


def __starting_point():
    main()


__starting_point()
