import sys
input = sys.stdin.readline
for nt in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
        continue
    dp = [[0, 0] for i in range(n)]
    dp[0][0] = a[0]
    dp[1][0] = max(a[0], a[1])
    dp[1][1] = max(0, a[0] - a[1])
    for i in range(2, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + a[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - a[i])
    print(max(dp[-1][0], dp[-1][1]))
