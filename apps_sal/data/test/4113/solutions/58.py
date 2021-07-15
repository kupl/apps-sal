n = int(input())
dp = [False] * (n+10)
dp[0] = True
for i in range(n):
    if dp[i]:
        dp[i+4]=True
        dp[i+7]=True
if dp[n]:
    print('Yes')
else:
    print('No')
