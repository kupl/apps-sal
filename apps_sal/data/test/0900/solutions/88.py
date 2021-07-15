s = input()
 
mod = 10**9+7
n = len(s)
res = [1] + [0] * 12
for ss in s:
    dp = [0] * 13
    for i in range(13):
        dp[(10*i)%13] = res[i]
    dp += dp
 
    if ss == '?':
        for i in range(13):
            res[i] = sum(dp[i+4:i+14])
    else:
        for i in range(13):
            res[i] = dp[i+13-int(ss)]
    res = [v%mod for v in res]
print(res[5])
