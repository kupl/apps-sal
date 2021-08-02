def main():
    N = int(input())
    A = list(map(int, input().split()))

    dp = [[0] * (N + 1 - i) for i in range(N + 1)]

    A = list(enumerate(A))
    A.sort(key=lambda x: x[1])
    ans = 0
    for z in range(1, N + 1):
        tmp = A.pop()
        i = tmp[0] + 1
        a = tmp[1]
        for x in range(z + 1):
            y = z - x
            if x == 0:
                dp[x][y] = max(dp[x][y - 1] + a * abs(i - (N - y + 1)), dp[x][y])
            elif y == 0:
                dp[x][y] = max(dp[x - 1][y] + a * abs(i - x), dp[x][y])
            else:
                dp[x][y] = max(dp[x][y - 1] + a * abs(i - (N - y + 1)), dp[x][y], dp[x - 1][y] + a * abs(i - x))
            ans = max(ans, dp[x][y])
    print(ans)


def __starting_point():
    main()


__starting_point()
