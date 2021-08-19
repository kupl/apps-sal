from sys import stdin
t = int(stdin.readline().strip())
for Ta in range(t):
    (n, a, b) = list(map(int, stdin.readline().strip().split()))
    s = stdin.readline().strip()
    dp = [[10 ** 15, 10 ** 15] for i in range(n)]
    dp[0][0] = a + b
    dp[0][1] = b + 2 * a
    for i in range(1, n):
        if s[i] == '0':
            dp[i][0] = min(dp[i - 1][0] + a + b, dp[i - 1][1] + 2 * a + 2 * b)
            dp[i][1] = min(dp[i - 1][0] + b + 2 * a, dp[i - 1][1] + 2 * b + a)
        else:
            dp[i][1] = dp[i - 1][1] + 2 * b + a
    print(dp[-1][0] + b)
