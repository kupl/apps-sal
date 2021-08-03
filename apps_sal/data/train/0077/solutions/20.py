import sys
import math
INF = float("inf")


def main():
    def input():
        return sys.stdin.readline()[:-1]
    q = int(input())
    for _ in range(q):
        n = int(input())
        w = [list(map(int, input().split())) for k in range(n)]
        dp = [[INF, INF, INF] for k in range(n)]
        dp[0] = [0, w[0][1], 2 * w[0][1]]
        for k in range(1, n):
            for l in range(3):
                for m in range(3):
                    if w[k - 1][0] + l != w[k][0] + m:
                        dp[k][m] = min(dp[k][m], dp[k - 1][l] + w[k][1] * m)
        print(min(dp[n - 1]))


def __starting_point():
    main()


__starting_point()
