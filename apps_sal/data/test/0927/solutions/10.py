n, m = map(int, input().split())
a = list(map(int, input().split()))
l = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-1] * (n+1)
dp[0] =  0

for i in range(n+1):
    for j in a:
        if i + l[j] < n+1:
            dp[i + l[j]] = max(dp[i + l[j]], dp[i]*10 + j)
print(dp[-1])
