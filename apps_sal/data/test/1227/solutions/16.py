sN = input()
K = int(input())
N = int(sN)


def run():
    dp = [[[0] * 4 for _ in range(2)] for _ in range(len(sN) + 1)]
    dp[0][0][0] = 1

    for i in range(len(sN)):
        for j in range(2):
            # j=0 : 現在の桁まで数字が同じ
            # j=1 : すでに小さい数値とわかっている

            # limには次の桁の数字の最大値を代入する
            lim = 9 if j == 1 else (ord(sN[i]) - ord('0'))
            for k in range(lim + 1):
                for l in range(4):
                    nl = l + int(k > 0)
                    if nl >= 4: continue
                    dp[i + 1][k < lim or j == 1][nl] += dp[i][j][l]

        # print(dp)

    print((dp[len(sN)][0][K] + dp[len(sN)][1][K]))


def __starting_point():
    run()


__starting_point()
