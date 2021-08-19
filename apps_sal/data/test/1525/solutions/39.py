"""
    dp[h][w]: h番目のrow(h: 0~H(終着))で棒w(w: 0~W-1)にいる状態になるための横線(0~h)の組合せ数
    dp[h][w] = A*dp[h-1][w-1] + B*dp[h-1][w] + C*dp[h-1][w+1] O(100*8)
    A, B, Cはなんかうまいこと決めれそう。(全探索でもO(7*7*7))
    """


def main():
    import sys
    input = sys.stdin.readline
    (H, W, K) = map(int, input().split())
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for h in range(1, H + 1):
        for w in range(W):
            (A, B, C) = (0, 0, 0)
            for i in range(2 ** (W - 1)):
                lines = []
                for j in range(W - 1):
                    if i >> j & 1:
                        if lines and lines[-1]:
                            break
                        lines.append(True)
                    else:
                        lines.append(False)
                else:
                    if w - 1 >= 0 and lines[w - 1]:
                        A += 1
                    elif w <= W - 2 and lines[w]:
                        C += 1
                    else:
                        B += 1
            if w - 1 >= 0:
                dp[h][w] += dp[h - 1][w - 1] * A
            dp[h][w] += dp[h - 1][w] * B
            if w + 1 <= W - 1:
                dp[h][w] += dp[h - 1][w + 1] * C
    print(dp[H][K - 1] % (10 ** 9 + 7))


def __starting_point():
    main()


__starting_point()
