import sys
mod = 7 + 10 ** 9


def solve():
    input = sys.stdin.readline
    H, W, K = map(int, input().split())
    DP = [[0] * W for _ in range(H + 1)]
    pattern = [1, 2, 3, 5, 8, 13, 21]
    DP[0][0] = 1
    for h in range(H):
        for w in range(W):
            if w == 0:
                DP[h + 1][w] += (DP[h][w] * pattern[max(0, W - 2)]) % mod
                if W > 1:
                    DP[h + 1][w] += (DP[h][w + 1] * pattern[max(0, W - 3)]) % mod
            elif w == W - 1:
                DP[h + 1][w] += (DP[h][w] * pattern[max(0, W - 2)]) % mod
                if W > 1:
                    DP[h + 1][w] += (DP[h][w - 1] * pattern[max(0, W - 3)]) % mod
            else:
                DP[h + 1][w] += (DP[h][w] * pattern[max(0, w - 1)] * pattern[max(0, W - w - 2)]) % mod
                DP[h + 1][w] += (DP[h][w + 1] * pattern[max(0, w - 1)] * pattern[max(0, W - w - 3)]) % mod
                DP[h + 1][w] += (DP[h][w - 1] * pattern[max(0, w - 2)] * pattern[max(0, W - w - 2)]) % mod
            DP[h + 1][w] %= mod
    print(DP[H][K - 1])

    return 0


def __starting_point():
    solve()


__starting_point()
