import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7


def main():
    H, W, K = map(int, input().split())
    dp = [[0] * W for _ in range(H + 1)]  # 数え上げ問題なので0で初期化する
    dp[0][0] = 1  # 初期条件
    for h in range(H):
        for bit in range(1 << (W - 1)):  # 左ビットシフトで2 ** (W-1)と同じ
            if '11' in bin(bit):
                continue  # ある頂点から左右方向に棒が伸びているケースはスルー
            for w in range(W):
                # w番目の棒を考える
                if w and bit & (1 << (w - 1)):  # leftを見るので1<<w-1と確認, w=0の時はleftにいけないことに注意する
                    dp[h + 1][w - 1] += dp[h][w] % MOD
                elif bit & (1 << w):  # rightを見るので1<<w確認
                    dp[h + 1][w + 1] += dp[h][w] % MOD
                else:  # down, 左右どちらにもいかない時
                    dp[h + 1][w] += dp[h][w] % MOD
    # for i in dp:
    #     print(*i)
    print(dp[H][K - 1] % MOD)


def __starting_point():
    main()


__starting_point()
