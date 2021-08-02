from operator import itemgetter


def main():
    n = int(input())
    a = sorted(enumerate(map(int, input().split())), key=itemgetter(1), reverse=True)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for x in range(n):
        for y in range(n - x):
            i, ai = a[x + y]
            dp[x + 1][y] = max(ai * (i - x) + dp[x][y], dp[x + 1][y])
            dp[x][y + 1] = max(ai * (n - 1 - y - i) + dp[x][y], dp[x][y + 1])
    print(max(dp[i][n - i] for i in range(n)))


def __starting_point():
    main()


__starting_point()
