n = int(input())
a = [int(x) for x in input().split()]
a += [0]

dp = [0] * (n + 5)
i = n - 2
dp[n - 1] = 1
while (i >= 0):
    if (a[i] < a[i + 1]):
        dp[i] = dp[i + 1] + 1
    else:
        dp[i] = 1
    i -= 1

temp = 1
ans = 1
for i in range(1, n):
    if a[i + 1] > a[i - 1]:
        ans = max(ans, temp + dp[i + 1])
    if a[i] > a[i - 1]:
        temp += 1
    else:
        temp = 1
    ans = max(ans, temp)

print(ans)
