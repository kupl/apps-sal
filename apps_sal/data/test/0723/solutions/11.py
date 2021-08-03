import math
def R(): return map(int, input().split())


n = int(input())
arr = []
for i in range(n):
    h, w = R()
    arr.append([h, w])
dp = [[math.inf] * 1001 for i in range(n)] + [[0] * 1001]
for i in range(n):
    for j in range(1001):
        if j >= max(arr[i]):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + j * min(arr[i]))
        elif j >= min(arr[i]):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + j * max(arr[i]))
print(min(dp[n - 1]))
