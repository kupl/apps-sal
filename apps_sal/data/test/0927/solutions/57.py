n, m = map(int, input().split()) 
a = list(map(int, input().split()))
b = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = [-1] * (n + 1)
dp[n] = 0

for i in range(n, -1, -1):
    for j in range(m):
        x = b[a[j]]
        if dp[i] != -1 and i - x >= 0:
            dp[i - x] = max(dp[i - x], 10 * dp[i] + a[j])
            
print(dp[0])
