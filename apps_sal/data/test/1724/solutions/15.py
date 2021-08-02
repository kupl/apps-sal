n = int(input())
a = list(map(int, input().split()))
s = input()
m = len(s)

prevSum = [0] * n
prevSum[0] = a[0]
for i in range(1, n):
    prevSum[i] = prevSum[i - 1] + a[i]

dp = [0] * m
lastOne = -1
if (s[0] != "0"):
    lastOne = 0
    dp[0] = a[0]

for i in range(1, m):
    if (s[i] == "0"):
        dp[i] = dp[i - 1]
    else:
        y = 0
        if (lastOne != -1):
            y = dp[lastOne]
        dp[i] = max(prevSum[i - 1], y + a[i])
        lastOne = i

print(dp[m - 1])
