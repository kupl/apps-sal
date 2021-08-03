from sys import stdin
input = stdin.readline
q = int(input())
for rwe in range(q):
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        x, y = map(int, input().split())
        a[i] = x
        b[i] = y
    dp = [[0, 0, 0] for i in range(n)]
    dp[0][0] = 0
    dp[0][1] = b[0]
    dp[0][2] = 2 * b[0]
    for i in range(1, n):
        for pod in range(3):
            x = (dp[i - 1][0] if a[i - 1] != a[i] + pod else 100000000000000000000000000)
            y = (dp[i - 1][1] if a[i - 1] + 1 != a[i] + pod else 10000000000000000000000000000)
            z = (dp[i - 1][2] if a[i - 1] + 2 != a[i] + pod else 10000000000000000000000000000)
            dp[i][pod] = min(x, y, z) + pod * b[i]
    print(min(dp[n - 1]))
