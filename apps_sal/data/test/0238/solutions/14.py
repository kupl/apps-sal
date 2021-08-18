'''input
5 3 10
1 2 10 2 3
'''
import math


def max_sub(arr, n):
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + arr[i], arr[i])
    return max(0, max(dp))


n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
q = -math.inf
dp = [0] * (300100)
for i in range(300100):
    dp[i] = [q] * (11)
if (m == 1):
    for i in range(n):
        arr[i] = arr[i] - k
    print(max_sub(arr, n))
else:
    for i in range(n):
        dp[i][1] = arr[i] - k
        for j in range(m):
            if (i - 1 < 0 or dp[i - 1][j] == q):
                continue
            if ((j + 1) % m != 1):
                dp[i][(j + 1) % m] = dp[i - 1][j] + arr[i]
            else:
                dp[i][(j + 1) % m] = max(arr[i] - k, dp[i - 1][j] + arr[i] - k)
    ma = 0
    for i in range(n):
        for j in range(m):
            ma = max(ma, dp[i][j])
    print(ma)
