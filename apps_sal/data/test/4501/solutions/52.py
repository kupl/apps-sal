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

    neg = pos = 0
    for x in X:
        if x > 0:
            pos += x
        else:
            neg += x

    M = pos - neg
    base = -neg

    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][base] = 1

    for i in range(N):
        for s in range(M + 1):
            dp[i + 1][s] = dp[i][s]
            if 0 <= s - X[i] <= M:
                dp[i + 1][s] += dp[i][s - X[i]]

    print((dp[N][base] - 1))
    return


def __starting_point():
    main()

__starting_point()
