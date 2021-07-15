N = int(input())
dp = [[0 for i in range(10)] for j in range(10)]
 
for i in range(1, N + 1):
    i = str(i)
    dp[int(i[0])][int(i[-1])] += 1
 
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += dp[i][j] * dp[j][i]
print(ans)
