from sys import setrecursionlimit, exit
setrecursionlimit(1000000000)


def main():
    n = int(input())
    a = [(int(v), i) for (i, v) in enumerate(input().split())]
    a.sort(reverse=True)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = a[0][0] * (n - 1 - a[0][1])
    dp[0][1] = a[0][0] * a[0][1]
    for (i, v) in enumerate(a[1:]):
        dp[i + 1][0] = dp[i][0] + v[0] * abs(n - 1 - (i + 1) - v[1])
        dp[i + 1][i + 2] = dp[i][i + 1] + v[0] * abs(v[1] - (i + 1))
        for j in range(1, i + 2):
            dp[i + 1][j] = max(dp[i][j] + v[0] * abs(n - 1 - (i + 1) + j - v[1]), dp[i][j - 1] + v[0] * abs(v[1] - (j - 1)))
    ans = -float('inf')
    for i in dp[n - 1]:
        ans = max(ans, i)
    print(ans)


main()
