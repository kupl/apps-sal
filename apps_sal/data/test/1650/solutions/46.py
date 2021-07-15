l = input()
dp = [1, 0]
mod = 10**9+7
for i in l:
    newdp = dp[:]
    if i=='0':
        newdp[0] = dp[0]
        newdp[1] = dp[1]*3%mod
    else:
        newdp[0] = dp[0]*2%mod
        newdp[1] = (dp[0]+dp[1]*3)%mod
    dp = newdp
print(sum(dp)%mod)
