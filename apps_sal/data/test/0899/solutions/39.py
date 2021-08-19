def main():
    import sys
    readlines = sys.stdin.readlines
    (N, M) = list(map(int, input().split()))
    edge = []
    dp = [[10 ** 9] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    for s in readlines():
        (a, b, c) = list(map(int, s.split()))
        a -= 1
        b -= 1
        edge.append((a, b, c))
        dp[a][b] = c
        dp[b][a] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    cnt = 0
    for (a, b, c) in edge:
        if dp[a][b] < c:
            cnt += 1
    print(cnt)


def __starting_point():
    main()


__starting_point()
