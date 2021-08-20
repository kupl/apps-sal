def tc():
    (n, m) = list(map(int, input().split()))
    mat = [input() for _ in range(n)]
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    dp = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if j == 0 or j == m - 1 or i < 2:
                dp[i][j] = 1
            elif mat[i][j] == mat[i - 1][j] and mat[i][j] == mat[i - 1][j - 1] and (mat[i][j] == mat[i - 1][j + 1]) and (mat[i][j] == mat[i - 2][j]):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1], dp[i - 2][j]) + 1
            else:
                dp[i][j] = 1
            ans += dp[i][j]
    print(ans)


tc()
