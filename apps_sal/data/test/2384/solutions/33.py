def resolve():
    INF = float('-inf')
    N = int(input())
    A = list(map(int, input().split()))
    skip = 1 + N % 2
    dp = [[INF] * (skip + 1) for _ in range(N + 2)]
    dp[0][0] = 0
    for i in range(N + 1):
        for j in range(skip + 1):
            if j < skip:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
            if i < N:
                dp[i + 2][j] = max(dp[i + 2][j], dp[i][j] + A[i])
    print(dp[N + 1][skip])


def __starting_point():
    resolve()


__starting_point()
