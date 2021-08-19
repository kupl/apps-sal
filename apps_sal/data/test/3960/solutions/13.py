n = int(input())
nums = input().split(' ')
sumas = [0] * (n + 1)
dp = [[0] * 2 for _ in range(n + 1)]
res = -100000000000.0
for x in range(0, n):
    if x > 0:
        sumas[x] = abs(int(nums[x]) - int(nums[x - 1]))
for x in range(1, n + 1):
    dp[x][0] = max(sumas[x], dp[x - 1][1] + sumas[x])
    dp[x][1] = max(-sumas[x], dp[x - 1][0] - sumas[x])
    res = max(max(dp[x][0], dp[x][1]), res)
print(res)
