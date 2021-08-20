def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted([(a, i) for (i, a) in enumerate(A)], reverse=True)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for (i, (a, p)) in enumerate(A):
        for j in range(i + 1):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (p - j) * a)
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + (N - (i - j) - 1 - p) * a)
    print(max(dp[-1]))


def __starting_point():
    resolve()


__starting_point()
