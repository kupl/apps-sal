def main():
    N = int(input())
    A = list(map(int, input().split()))
    AA = [(v, i) for (i, v) in enumerate(A)]
    AA.sort(reverse=True)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for (i, (a, b)) in enumerate(AA, start=1):
        for x in range(i + 1):
            y = i - x
            if y == 0:
                dp[x][y] = dp[x - 1][y] + abs(b - x + 1) * a
            elif x == 0:
                dp[x][y] = dp[x][y - 1] + abs(N - y - b) * a
            else:
                dp[x][y] = max(dp[x - 1][y] + abs(b - x + 1) * a, dp[x][y - 1] + abs(N - y - b) * a)
    r = 0
    for i in range(N + 1):
        r = max(r, dp[i][N - i])
    return r


print(main())
