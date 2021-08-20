import sys
from itertools import combinations
input = sys.stdin.readline


def main():
    (n, ma, mb) = list(map(int, input().split()))
    dp = [[0] * 401 for _ in range(401)]
    for _ in range(n):
        (a, b, c) = list(map(int, input().split()))
        for i in range(400, -1, -1):
            for j in range(400, -1, -1):
                if i == 0 and j == 0:
                    if dp[a][b]:
                        dp[a][b] = min(dp[a][b], c)
                    else:
                        dp[a][b] = c
                if dp[i][j] and i + a <= 400 and (j + b <= 400):
                    if dp[i + a][j + b]:
                        dp[i + a][j + b] = min(dp[i + a][j + b], dp[i][j] + c)
                    else:
                        dp[i + a][j + b] = dp[i][j] + c
    ans = 1000000
    (x, y) = (ma, mb)
    while x <= 400 and y <= 400:
        if dp[x][y]:
            ans = min(dp[x][y], ans)
        x += ma
        y += mb
    if ans == 1000000:
        print(-1)
    else:
        print(ans)


def __starting_point():
    main()


__starting_point()
