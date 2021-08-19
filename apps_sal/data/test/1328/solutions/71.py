import sys
input = sys.stdin.readline


def main():
    (N, Ma, Mb) = list(map(int, input().split()))
    abc = [list(map(int, input().split())) for i in range(N)]
    INF = N * 100 + 1
    dp = [[[INF for cb in range(411)] for ca in range(411)] for i in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for ca in range(N * 10):
            for cb in range(N * 10):
                if dp[i][ca][cb] == INF:
                    continue
                dp[i + 1][ca][cb] = min(dp[i + 1][ca][cb], dp[i][ca][cb])
                d = abc[i]
                dp[i + 1][ca + d[0]][cb + d[1]] = min(dp[i + 1][ca + d[0]][cb + d[1]], dp[i][ca][cb] + d[2])
    res = INF
    for ca in range(1, 401):
        for cb in range(1, 401):
            if ca * Mb == cb * Ma:
                res = min(res, dp[N][ca][cb])
    if res == INF:
        res = -1
    print(res)


main()
