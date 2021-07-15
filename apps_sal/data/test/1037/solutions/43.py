from sys import stdin


def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    a2 = [[a[i], i] for i in range(n)]
    a2.sort(reverse=True)

    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    ans = 0

    for i in range(n + 1):
        for j in range(n + 1 - i):
            s1 = s2 = 0
            if i > 0:
                s1 = dp[i - 1][j] + a2[i + j - 1][0] * (a2[i + j - 1][1] - (i - 1))
            if j > 0:
                s2 = dp[i][j - 1] + a2[i + j - 1][0] * ((n - j) - a2[i + j - 1][1])
            dp[i][j] = max(s1, s2)
        ans = max(ans, dp[i][n - i])

    print(ans)


def __starting_point():
    main()

__starting_point()
