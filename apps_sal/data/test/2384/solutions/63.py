import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = list(map(int, read().split()))

    skip = 1 + N % 2
    dp = [[-INF] * (skip + 1) for _ in range(N + 2)]
    dp[0][0] = 0

    for i in range(N + 1):
        for j in range(skip + 1):
            if j < skip and dp[i + 1][j + 1] < dp[i][j]:
                dp[i + 1][j + 1] = dp[i][j]
            if i < N and dp[i + 2][j] < dp[i][j] + A[i]:
                dp[i + 2][j] = dp[i][j] + A[i]

    print((dp[N + 1][skip]))

    return


def __starting_point():
    main()


__starting_point()
