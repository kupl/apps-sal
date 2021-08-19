import sys
readline = sys.stdin.readline
MOD = 10 ** 9 + 7


def main():
    H, W, K = map(int, readline().rstrip().split())
    # K -= 1
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            for k in range(2**(W - 1)):
                b = bin(k)[2:].zfill(W - 1)
                # 2つの横線がつながってないか調べる
                flg = True
                for l in range(W - 2):
                    if b[l] == b[l + 1] == '1':
                        flg = False
                        break
                if not flg:
                    continue
                if j >= 1 and b[j - 1] == '1':
                    # 左方向に横線を辿るケース
                    dp[i + 1][j - 1] += dp[i][j]
                    dp[i + 1][j - 1] %= MOD
                elif j <= W - 2 and b[j] == '1':
                    # 右方向に横線を辿るケース
                    dp[i + 1][j + 1] += dp[i][j]
                    dp[i + 1][j + 1] %= MOD
                else:
                    # 横線を辿らないケース
                    dp[i + 1][j] += dp[i][j]
                    dp[i + 1][j] %= MOD

    print(dp[H][K - 1])


def __starting_point():
    main()


__starting_point()
