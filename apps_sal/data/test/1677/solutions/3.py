n = int(input())
a = list(map(int, input().split()))
dp=[[0 for i in range(n+1)] for i in range(n+1)]
ans = 0
pre = 0
a = [0] + a
for i in range(1, n+1):
    pre = 0
    for j in range(i):
        dp[i][j] = dp[j][pre]+1
        if a[i] == a[j]:
            pre = j
        ans = max(ans, dp[i][j])
print(ans)
