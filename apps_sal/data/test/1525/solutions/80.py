import sys
from itertools import product

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, W, K = list(map(int, readline().split()))

    A = product((0, 1), repeat=W - 1)
    B = []
    for bars in A:
        ok = True
        for i in range(W - 2):
            if bars[i] and bars[i + 1]:
                ok = False
                break
        if ok:
            B.append(bars)

    dp = [0] * W
    dp[0] = 1

    for _ in range(H):
        dp, dp_prev = [0] * W, dp
        for bars in B:
            for i in range(W):
                if i > 0 and bars[i - 1]:
                    dp[i - 1] = (dp[i - 1] + dp_prev[i]) % MOD
                elif i < W - 1 and bars[i]:
                    dp[i + 1] = (dp[i + 1] + dp_prev[i]) % MOD
                else:
                    dp[i] = (dp[i] + dp_prev[i]) % MOD

    print((dp[K - 1]))

    return


def __starting_point():
    main()

__starting_point()
