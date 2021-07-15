n = int(input())
a = input()
dp = [0] * n
for i in range(n):
    if (a[i] == 'W'):
        dp[i] = 0
    else:
        dp[i] = dp[i - 1] + 1
dp += [0]
ans = []
for i in range(n):
    if (dp[i] != 0 and dp[i + 1] == 0):
        ans.append(dp[i])
print(len(ans))
print(*ans)
