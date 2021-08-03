import sys
input = sys.stdin.readline

q = int(input())
for i in range(q):
    n = int(input())
    dp = [[0] * n for _ in range(3)]
    prev = 0
    for i in range(n):
        l, c = [int(item) for item in input().split()]
        if i == 0:
            dp[0][0] = 0
            dp[1][0] = c
            dp[2][0] = c * 2
            prev = l
            continue
        prev_min = min(dp[0][i - 1], dp[1][i - 1], dp[2][i - 1])
        if l > prev + 2:
            dp[0][i] = prev_min
            dp[1][i] = prev_min + c
            dp[2][i] = prev_min + c * 2
        elif l == prev + 2:
            dp[0][i] = min(dp[0][i - 1], dp[1][i - 1])
            dp[1][i] = prev_min + c
            dp[2][i] = prev_min + c * 2
        elif l == prev + 1:
            dp[0][i] = min(dp[0][i - 1], dp[2][i - 1])
            dp[1][i] = min(dp[0][i - 1], dp[1][i - 1]) + c
            dp[2][i] = prev_min + c * 2
        elif l == prev:
            dp[0][i] = min(dp[1][i - 1], dp[2][i - 1])
            dp[1][i] = min(dp[0][i - 1], dp[2][i - 1]) + c
            dp[2][i] = min(dp[0][i - 1], dp[1][i - 1]) + 2 * c
        elif l == prev - 1:
            dp[0][i] = prev_min
            dp[1][i] = min(dp[1][i - 1], dp[2][i - 1]) + c
            dp[2][i] = min(dp[0][i - 1], dp[2][i - 1]) + 2 * c
        elif l == prev - 2:
            dp[0][i] = prev_min
            dp[1][i] = prev_min + c
            dp[2][i] = min(dp[1][i - 1], dp[2][i - 1]) + 2 * c
        elif l < prev - 2:
            dp[0][i] = prev_min
            dp[1][i] = prev_min + c
            dp[2][i] = prev_min + c * 2
        prev = l
    print(min(dp[0][n - 1], dp[1][n - 1], dp[2][n - 1]))
