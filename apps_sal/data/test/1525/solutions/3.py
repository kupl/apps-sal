import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7


def main():
    H, W, K = map(int, input().split())
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for h in range(H):
        for bit in range(1 << (W - 1)):
            if '11' in bin(bit):
                continue
            for w in range(W):
                if w and bit & (1 << (w - 1)):
                    dp[h + 1][w - 1] += dp[h][w] % MOD
                elif bit & (1 << w):
                    dp[h + 1][w + 1] += dp[h][w] % MOD
                else:
                    dp[h + 1][w] += dp[h][w] % MOD
    print(dp[H][K - 1] % MOD)


def __starting_point():
    main()


__starting_point()
