n = int(input())
c = list(map(int, input().split()))
a = []
for _ in range(n):
    a.append(input())

dp = [[1000000000000000000] * 2 for x in range(200000)]
# print(dp)
dp[0][0] = 0
dp[0][1] = c[0]

for i in range(1, n):
    if a[i - 1] <= a[i] and dp[i - 1][0] < dp[i][0]:
        dp[i][0] = dp[i - 1][0]
    if a[i - 1][::-1] <= a[i] and dp[i - 1][1] < dp[i][0]:
        dp[i][0] = dp[i - 1][1]
    if a[i - 1] <= a[i][::-1] and dp[i - 1][0] + c[i] < dp[i][1]:
        dp[i][1] = dp[i - 1][0] + c[i]
    if a[i - 1][::-1] <= a[i][::-1] and dp[i - 1][1] + c[i] < dp[i][1]:
        dp[i][1] = dp[i - 1][1] + c[i]


if dp[n - 1][0] == 1000000000000000000 and dp[n - 1][1] == 1000000000000000000:
    print(-1)
    return
print(min(dp[n - 1][0], dp[n - 1][1]))
