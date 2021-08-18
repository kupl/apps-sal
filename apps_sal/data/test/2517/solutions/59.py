import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, M, R = list(map(int, input().split()))
    r = list(map(int, input().split()))
    P = permutations(r)

    dp = [[INF] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0

    for _ in range(M):
        a, b, c = list(map(int, input().split()))
        a -= 1
        b -= 1
        dp[a][b] = c
        dp[b][a] = c

    for k in range(N):
        for i in range(N):
            for j in range(N):
                tmp = dp[i][k] + dp[k][j]
                if tmp < dp[i][j]:
                    dp[i][j] = tmp

    ans = INF
    for p in P:
        tmp = 0
        for i in range(R - 1):
            tmp += dp[p[i] - 1][p[i + 1] - 1]

        if tmp < ans:
            ans = tmp

    print(ans)


def __starting_point():
    main()


__starting_point()
