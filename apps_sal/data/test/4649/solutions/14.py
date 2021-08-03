q = int(input())
for t in range(q):
    n, k = list(map(int, input().split()))
    rgb = input()
    dp = [0] * 3
    dp[0] = [0] * (n + 1)
    dp[1] = [0] * (n + 1)
    dp[2] = [0] * (n + 1)
    for i in range(0, n):
        if rgb[i] == 'R':
            dp[0][i + 1] = dp[2][i]
            dp[1][i + 1] = dp[0][i] + 1
            dp[2][i + 1] = dp[1][i] + 1
        if rgb[i] == 'G':
            dp[0][i + 1] = dp[2][i] + 1
            dp[1][i + 1] = dp[0][i]
            dp[2][i + 1] = dp[1][i] + 1
        if rgb[i] == 'B':
            dp[0][i + 1] = dp[2][i] + 1
            dp[1][i + 1] = dp[0][i] + 1
            dp[2][i + 1] = dp[1][i]
    repl = k
    dif = k % 3
    for j in range(3):
        for i in range(1, n - k + 2):
            repl = min(repl, -dp[j][i - 1] + dp[(j + dif) % 3][i + k - 1])
    print(repl)
