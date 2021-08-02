def main():
    N, A = list(map(int, input().split()))
    X = list(map(int, input().split()))

    dp = [[0] * (A * N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i, x in enumerate(X):
        for j in reversed(list(range(1, i + 2))):
            for a in range(x, A * N + 1):
                dp[j][a] += dp[j - 1][a - x]
    return sum(dp[i][A * i] for i in range(1, N + 1))


print((main()))
