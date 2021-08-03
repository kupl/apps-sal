import sys

input = sys.stdin.readline


def main():
    H, W, K = [int(x) for x in input().split()]
    MOD = 10 ** 9 + 7

    if W == 1:
        print((1))
        return

    cnt = [0] * (W - 1)
    cntz = [0] * W
    for i in range(2 ** (W - 1)):
        tmp = [0] * (W - 1)
        for j in range(W - 1):
            if i >> j & 1:
                tmp[j] += 1
        # 2辺連続で引かれていないかをチェック
        for j, k in zip(tmp, tmp[1:]):
            if j == k == 1:
                break
        else:
            # チェックをパスした状態をカウント
            for j in range(W - 1):
                cnt[j] += tmp[j]
            for j in range(W):
                if j == 0:
                    if tmp[j] == 0:
                        cntz[j] += 1
                elif j == W - 1:
                    if tmp[j - 1] == 0:
                        cntz[j] += 1
                else:
                    if tmp[j] == tmp[j - 1] == 0:
                        cntz[j] += 1

    dp = [[0] * W for j in range(H + 1)]
    dp[0][0] = 1

    for j in range(H):
        for i in range(W):
            if i == 0:
                dp[j + 1][i] += dp[j][i] * cntz[i]
                dp[j + 1][i + 1] += dp[j][i] * cnt[i]
                dp[j + 1][i] %= MOD
                dp[j + 1][i + 1] %= MOD
            elif i == W - 1:
                dp[j + 1][i] += dp[j][i] * cntz[i]
                dp[j + 1][i - 1] += dp[j][i] * cnt[i - 1]
                dp[j + 1][i] %= MOD
                dp[j + 1][i - 1] %= MOD
            else:
                dp[j + 1][i] += dp[j][i] * cntz[i]
                dp[j + 1][i + 1] += dp[j][i] * cnt[i]
                dp[j + 1][i - 1] += dp[j][i] * cnt[i - 1]
                dp[j + 1][i] %= MOD
                dp[j + 1][i + 1] %= MOD
                dp[j + 1][i - 1] %= MOD

    print((dp[-1][K - 1]))


def __starting_point():
    main()


__starting_point()
