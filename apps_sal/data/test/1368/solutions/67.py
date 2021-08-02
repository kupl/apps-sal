import sys
input = sys.stdin.readline


def main():
    n, a, b = list(map(int, input().split()))
    v = list(map(int, input().split()))

    dp = [[0, 0] for _ in range(n + 1)]
    dp[0][1] = 1
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if dp[j][1]:
                if dp[j + 1][0] < dp[j][0] + v[i]:
                    dp[j + 1][0] = dp[j][0] + v[i]
                    dp[j + 1][1] = dp[j][1]
                elif dp[j + 1][0] == dp[j][0] + v[i]:
                    dp[j + 1][1] += dp[j][1]

    index, value, count = a, dp[a][0], dp[a][1]
    for i in range(a + 1, b + 1):
        if value * i == index * dp[i][0]:
            count += dp[i][1]
        elif value * i < index * dp[i][0]:
            value = dp[i][0]
            index = i
            count = dp[i][1]

    print((value / index))
    print(count)


def __starting_point():
    main()


__starting_point()
