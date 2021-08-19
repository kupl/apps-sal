INF = 10 ** 18


def read():
    return [int(x) for x in input().split()]


def main():
    (n,) = read()
    c = read()
    a = []
    b = []
    for i in range(0, n):
        s = input()
        a.append(s)
        b.append(s[::-1])
    dp = [[0, 0] for _ in range(0, n)]
    dp[0][0] = 0
    dp[0][1] = c[0]
    for i in range(1, n):
        dp[i][0] = INF
        dp[i][1] = INF
        if a[i] >= a[i - 1]:
            dp[i][0] = min(dp[i][0], dp[i - 1][0])
        if a[i] >= b[i - 1]:
            dp[i][0] = min(dp[i][0], dp[i - 1][1])
        if b[i] >= a[i - 1]:
            dp[i][1] = min(dp[i][1], dp[i - 1][0] + c[i])
        if b[i] >= b[i - 1]:
            dp[i][1] = min(dp[i][1], dp[i - 1][1] + c[i])
    res = min(dp[n - 1][0], dp[n - 1][1])
    print(res == INF and -1 or res)


main()
