n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    if a[i] >= a[i - 1]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = 1
print(max(dp))
