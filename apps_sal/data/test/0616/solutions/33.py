def solve(N, M, ABCi):
    inf = 10 ** 5 * 12 * 2
    for i in range(M):
        C = ABCi[i][2]
        ABCi[i][2] = sum([2 ** (c - 1) for c in C])
    dp = [[inf] * 2 ** N for _ in range(M + 1)]
    dp[0][0] = 0
    for i in range(1, M + 1):
        for j in range(2 ** N):
            (a, b, c) = ABCi[i - 1]
            dp[i][j] = min(dp[i - 1][c & j ^ j] + a, dp[i - 1][j])
    ans = min([x[2 ** N - 1] for x in dp])
    if ans == inf:
        ans = -1
    print(ans)


def __starting_point():
    (N, M) = list(map(int, input().split()))
    ABCi = [[int(i) for i in input().split()] + [[int(i) for i in input().split()]] for _ in range(M)]
    solve(N, M, ABCi)


__starting_point()
