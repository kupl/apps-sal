#!/usr/bin/env python2


def main():
    n, k = list(map(int, input().split()))
    a = sorted(int(i) for i in input().split())

    upper_bound = [0] * n

    i, j = 0, 0
    while j < n:
        if a[i] + 5 >= a[j]:
            j += 1
        else:
            i += 1
        upper_bound[i] = j

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(1, k + 1):
            x = upper_bound[i]
            dp[i][j] = max(1 + dp[i + 1][j - 1], dp[i + 1][j], x - i + dp[x][j - 1])

    print(dp[0][k])


def __starting_point():
    main()


__starting_point()
