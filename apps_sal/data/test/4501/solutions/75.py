def main():
    (N, A) = list(map(int, input().split()))
    x = list(map(int, input().split()))
    dp = [[0] * (50 * N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for k in range(N):
        for i in reversed(list(range(k + 1))):
            for j in range(50 * N + 1 - x[k]):
                dp[i + 1][j + x[k]] += dp[i][j]
    r = 0
    for i in range(1, N + 1):
        r += dp[i][i * A]
    return r


print(main())
