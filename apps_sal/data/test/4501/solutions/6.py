import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, A, *X = list(map(int, read().split()))

    X = [x - A for x in X]

    base = 2500
    dp = [0] * 5001
    dp[base] = 1
    for i in range(N):
        dp, dp_prev = dp[:], dp
        for j in range(5001):
            if 0 <= j - X[i] <= 5000:
                dp[j] += dp_prev[j - X[i]]

    print((dp[base] - 1))

    return


def __starting_point():
    main()

__starting_point()
