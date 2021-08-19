import math
a = [0] * 100005
dp = [0] * 100005
x = int(input(''))
y = input('').split(' ')
y = [int(z) for z in y]
for g in range(len(y)):
    a[y[g]] += 1
for g in range(100000, 0, -1):
    if dp[g + 1] > dp[g + 2] + g * a[g]:
        dp[g] = dp[g + 1]
    else:
        dp[g] = dp[g + 2] + g * a[g]
print(dp[1])
