INF = 10**18


def solve(n, a):
    # 現在の位置 x 選んだ個数 x 直前を選んだかどうか
    dp = [{j: [-INF, -INF] for j in range(i // 2 - 1, (i + 1) // 2 + 1)} for i in range(n + 1)]
    dp[0][0][False] = 0
    for i in range(n):
        for j in dp[i].keys():
            if (j + 1) in dp[i + 1]:
                dp[i + 1][j + 1][True] = max(dp[i + 1][j + 1][True], dp[i][j][False] + a[i])
            if j in dp[i + 1]:
                dp[i + 1][j][False] = max(dp[i + 1][j][False], dp[i][j][False])
                dp[i + 1][j][False] = max(dp[i + 1][j][False], dp[i][j][True])
    return max(dp[n][n // 2])


n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
