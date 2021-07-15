n, l, r = list(map(int, input().split()))
MOD = 10**9+7
l -= 1
lrem = [0, 0, 0]
rrem = [0, 0, 0]
rem = [0, 0, 0]
if l%3 == 0:
    lrem[0] = l//3
    lrem[1] = l//3
    lrem[2] = l//3
elif l%3 == 1:
    lrem[0] = l//3
    lrem[1] = l//3 + 1
    lrem[2] = l//3
else: 
    lrem[0] = l//3
    lrem[1] = l//3 + 1
    lrem[2] = l//3 + 1
if r%3 == 0:
    rrem[0] = r//3
    rrem[1] = r//3
    rrem[2] = r//3
elif r%3 == 1:
    rrem[0] = r//3
    rrem[1] = r//3 + 1
    rrem[2] = r//3
else:
    rrem[0] = r//3
    rrem[1] = r//3 + 1
    rrem[2] = r//3 + 1
    
rem[0] = rrem[0]-lrem[0]
rem[1] = rrem[1]-lrem[1]
rem[2] = rrem[2]-lrem[2]

dp = [[0 for i in range(n)] for i in range(3)]
dp[0][0] = rem[0]
dp[1][0] = rem[1]
dp[2][0] = rem[2]

for i in range(1, n):
    dp[0][i] = (dp[0][i-1]*rem[0] + dp[1][i-1]*rem[2] + dp[2][i-1]*rem[1])%MOD
    dp[1][i] = (dp[1][i-1]*rem[0] + dp[2][i-1]*rem[2] + dp[0][i-1]*rem[1])%MOD
    dp[2][i] = (dp[2][i-1]*rem[0] + dp[1][i-1]*rem[1] + dp[0][i-1]*rem[2])%MOD
print(dp[0][n-1])

