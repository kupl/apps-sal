def main():
    N = int(input())
    A = list(map(int, input().split()))
    AA = [(a, i) for (i, a) in enumerate(A)]
    AA.sort(reverse=True)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        (a, t) = AA[i]
        for x in range(i + 2):
            y = i + 1 - x
            dp[x][y] = max(dp[x - 1][y] + abs(t - (x - 1)) * a if x > 0 else 0, dp[x][y - 1] + abs(t - (N - y)) * a if y > 0 else 0)
    return max((dp[i][N - i] for i in range(N + 1)))


print(main())
