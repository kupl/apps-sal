def R():
    return map(int, input().split())


n = int(input())
arr = list(R())
dp = [[0] * (n + 1) for i in range(n + 1)]
for i in range(n):
    p = -1
    for j in range(i):
        dp[i][j] = max(dp[i][j], dp[j][p] + 1)
        p = j if arr[j] == arr[i] else p
print(max((max(dp[i]) for i in range(n))) + 1)
