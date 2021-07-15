N = int(input())

lst = [1, 6, 9, 6**2, 9**2, 6**3, 9**3, 6**4, 9**4, 6**5, 6**6, 9**5]
dp = [N+1] * (N+1)
dp[0] = 0
for i in range(1, N+1):
    for j in lst:
        if j <= i:
            # print(i, j, i-j)
            dp[i] = min(dp[i], dp[i-j]+1)
print(dp[-1])
