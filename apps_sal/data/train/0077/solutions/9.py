"""input
3
3
2 4
2 1
3 5
3
2 3
2 10
2 6
4
1 7
3 3
2 6
1000000000 2
"""
from sys import stdin
from math import ceil, log
q = int(stdin.readline().strip())
for _ in range(q):
    n = int(stdin.readline().strip())
    h = []
    c = []
    dp = dict()
    for i in range(n):
        (a, b) = list(map(int, stdin.readline().split()))
        h.append(a)
        c.append(b)
    dp = [[0 for x in range(3)] for y in range(n)]
    dp[0][0] = 0
    dp[0][1] = c[0]
    dp[0][2] = 2 * c[0]
    for i in range(1, n):
        if h[i] == h[i - 1]:
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + c[i]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + 2 * c[i]
        elif h[i] + 1 == h[i - 1]:
            dp[i][0] = min(dp[i - 1])
            dp[i][1] = min(dp[i - 1][1], dp[i - 1][2]) + c[i]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][2]) + 2 * c[i]
        elif h[i] + 2 == h[i - 1]:
            dp[i][0] = min(dp[i - 1])
            dp[i][1] = min(dp[i - 1]) + c[i]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + 2 * c[i]
        elif h[i] == h[i - 1] + 1:
            dp[i][0] = min(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + c[i]
            dp[i][2] = min(dp[i - 1]) + 2 * c[i]
        elif h[i] == h[i - 1] + 2:
            dp[i][0] = min(dp[i - 1][:2])
            dp[i][1] = min(dp[i - 1]) + c[i]
            dp[i][2] = min(dp[i - 1]) + 2 * c[i]
        else:
            dp[i][0] = min(dp[i - 1])
            dp[i][1] = min(dp[i - 1]) + c[i]
            dp[i][2] = min(dp[i - 1]) + 2 * c[i]
    print(min(dp[-1]))
