def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted([(a, i) for (i, a) in enumerate(A)], reverse=True)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        j = 0
        while i + j < N:
            (a, idx) = A[i + j]
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + (idx - i) * a)
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + (N - 1 - j - idx) * a)
            j += 1
    ans = 0
    for i in range(N + 1):
        ans = max(ans, dp[i][N - i])
    print(ans)


def __starting_point():
    resolve()


__starting_point()
