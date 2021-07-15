# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 0:18
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : E. K Balanced Teams.py


def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()

    cnt = [0] * n
    for i in range(n):
        while i + cnt[i] < n and a[i + cnt[i]] - a[i] <= 5:
            cnt[i] += 1

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(k + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + 1 <= k:
                dp[i + cnt[i]][j + 1] = max(dp[i + cnt[i]][j + 1], dp[i][j] + cnt[i])

    print(dp[n][k])


def __starting_point():
    main()

__starting_point()
