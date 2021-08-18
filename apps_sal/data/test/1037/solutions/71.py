def main():
    N = int(input())
    A = list(map(int, input().split()))

    Awithidx = [[a, i] for i, a in enumerate(A)]
    sortedA = sorted(Awithidx, reverse=True)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        a = sortedA[i][0]
        idx = sortedA[i][1]
        for l in range(i + 1):
            r = i - l
            dp[i + 1][l] = max(dp[i + 1][l], dp[i][l] + a * abs((N - r - 1) - idx))
            dp[i + 1][l + 1] = max(dp[i + 1][l + 1], dp[i][l] + a * abs(l - idx))
    print((max(dp[N])))


main()
