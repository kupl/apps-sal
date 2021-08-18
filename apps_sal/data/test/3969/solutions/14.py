import math
import sys
input = sys.stdin.readline
t = 1
for _ in range(t):
    n, m = list(map(int, input().split()))
    l = []
    for __ in range(n):
        s, x = list(map(float, input().split()))
        l.append(int(s))
    dp = [0] * (n + 1)
    for i in range(n):
        j = l[i]
        for j1 in range(j, -1, -1):
            dp[j] = max(dp[j], 1 + dp[j1])
    maxi = max(dp[:])
    print(n - maxi)
