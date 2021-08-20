def solve():
    INF = float('inf')

    def max2(x, y):
        return x if x >= y else y
    N = int(input())
    As = list(map(int, input().split()))
    dp = [[[-INF] * 2 for j in range(3)] for i in range(N + 1)]
    dp[0][2][0] = dp[0][2][1] = 0
    for (i, A) in enumerate(As):
        if i & 1:
            for k in range(2):
                for j in range(3):
                    dp[i + 1][j][0] = max2(dp[i + 1][j][0], dp[i][j][k])
            for j in range(2):
                dp[i + 1][j + 1][1] = max2(dp[i + 1][j + 1][1], dp[i][j][0] + A)
        else:
            for j in range(3):
                dp[i + 1][j][1] = max2(dp[i + 1][j][1], dp[i][j][0] + A)
            for k in range(2):
                for j in range(1, 3):
                    dp[i + 1][j - 1][0] = max2(dp[i + 1][j - 1][0], dp[i][j][k])
    if N & 1:
        print(max(dp[-1][1]))
    else:
        print(max(dp[-1][2]))


solve()
