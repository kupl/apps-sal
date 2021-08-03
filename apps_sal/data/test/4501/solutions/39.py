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
    dp = [[0] * 5001 for _ in range(N + 1)]
    dp[0][base] = 1
    for i in range(N):
        for j in range(-2500, 2501):
            if -2500 <= j - X[i] <= 2500:
                dp[i + 1][j + base] = dp[i][j + base] + dp[i][j - X[i] + base]
            else:
                dp[i + 1][j + base] = dp[i][j + base]

    print((dp[N][base] - 1))

    return


def __starting_point():
    main()


__starting_point()
