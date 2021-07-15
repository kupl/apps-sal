def main():
    N, *A = map(int, open(0).read().split())

    A = sorted(enumerate(A), reverse=True, key=lambda x: x[1])

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for l in range(N):
        for r in range(N - l):
            p, a = A[l + r]

            dp[l + 1][r] = max(
                dp[l + 1][r],
                a * (p - l) + dp[l][r]
            )
            dp[l][r + 1] = max(
                dp[l][r + 1],
                a * (N - 1 - r - p) + dp[l][r]
            )

    print(max(dp[l][N - l] for l in range(N)))

main()
