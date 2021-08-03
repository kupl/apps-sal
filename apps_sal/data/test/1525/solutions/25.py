import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, W, K = list(map(int, readline().split()))

    dp = [0] * W
    dp[0] = 1

    for _ in range(H):
        dp, dp_prev = [0] * W, dp
        for mask in range(1 << (W - 1)):
            ok = True
            for i in range(W - 2):
                if mask & (1 << i) and mask & (1 << (i + 1)):
                    ok = False
                    break
            if not ok:
                continue
            for i in range(W):
                if i > 0 and mask & (1 << (i - 1)):
                    dp[i - 1] = (dp[i - 1] + dp_prev[i]) % MOD
                elif i < W - 1 and mask & (1 << i):
                    dp[i + 1] = (dp[i + 1] + dp_prev[i]) % MOD
                else:
                    dp[i] = (dp[i] + dp_prev[i]) % MOD

    print((dp[K - 1]))

    return


def __starting_point():
    main()


__starting_point()
