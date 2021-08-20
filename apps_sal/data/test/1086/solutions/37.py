import numpy as np


def main():
    (h, w) = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [list(map(int, input().split())) for _ in range(h)]
    n = 80 * (80 + 80) + 10
    m = n // 2
    dp = [[None] * w for i in range(h)]
    for i in range(h):
        for j in range(w):
            dp[i][j] = np.zeros(n, np.bool)
    dp[0][0][m + abs(a[0][0] - b[0][0])] = True
    dp[0][0][m - abs(a[0][0] - b[0][0])] = True
    for i in range(h):
        for j in range(w):
            x = abs(a[i][j] - b[i][j])
            if 0 < i and 0 < h:
                dp[i][j][x:] |= dp[i - 1][j][:n - x]
                dp[i][j][:n - x] |= dp[i - 1][j][x:]
                dp[i][j][x:] |= dp[i][j - 1][:n - x]
                dp[i][j][:n - x] |= dp[i][j - 1][x:]
            elif 0 < i:
                dp[i][j][x:] |= dp[i - 1][j][:n - x]
                dp[i][j][:n - x] |= dp[i - 1][j][x:]
            elif 0 < j:
                dp[i][j][x:] |= dp[i][j - 1][:n - x]
                dp[i][j][:n - x] |= dp[i][j - 1][x:]
    ans = float('inf')
    for i in range(m - 80 - 1, m + 80 + 2):
        if dp[h - 1][w - 1][i]:
            ans = min(ans, abs(m - i))
    print(ans)


def __starting_point():
    main()


__starting_point()
