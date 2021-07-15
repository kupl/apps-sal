import sys
import numpy as np
N, K = map(int, sys.stdin.readline().rstrip().split())
A = np.array(list(map(int, sys.stdin.readline().rstrip().split())))
cnt = []

for i in range(41):
    cnt.append(np.count_nonzero(A >> i & 1))

cnt = cnt[::-1]
dp = [[0] * 2 for _ in range(42)]
ans = 0
base = 2**(41 - 1)

for i, c in enumerate(cnt, 1):
    if K >> (41 - i) & 1 == 1:
        dp[i][0] = dp[i - 1][0] + base * (N - c)
        if dp[i - 1][1] > 0:
            dp[i][1] = max(dp[i - 1][0] + base * c, dp[i - 1][1] + base * c,
                           dp[i - 1][1] + base * (N - c))
        else:
            dp[i][1] = dp[i - 1][0] + base * c

    else:
        dp[i][0] = dp[i - 1][0] + base * c
        if dp[i - 1][1] > 0:
            dp[i][1] = max(dp[i - 1][1] + base * c,
                           dp[i - 1][1] + base * (N - c))

    base //= 2

print(max(dp[41][0], dp[41][1]))
