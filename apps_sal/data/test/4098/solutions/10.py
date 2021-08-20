import io
import os
import sys


def main():
    (n, k) = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))
    maxFromI = [0] * n
    end = -1
    for i in range(n):
        while end + 1 < n and a[end + 1] <= a[i] + 5:
            end += 1
        maxFromI[i] = end - i + 1
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(k + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + 1 <= k:
                dp[i + maxFromI[i]][j + 1] = max(dp[i + maxFromI[i]][j + 1], dp[i][j] + maxFromI[i])
    print(dp[n][k])


def __starting_point():
    main()


__starting_point()
