import numpy as np
n = int(input())
dp = np.full(n + 1, n + 1, dtype=int)
dp[0] = 0
loop = 0
while dp[n] > n:
    tmp1 = np.full(n + 1, n + 1, dtype=int)
    tmp6 = np.full(n + 1, n + 1, dtype=int)
    tmp9 = np.full(n + 1, n + 1, dtype=int)
    tmp1[1:] = dp[:-1] + 1
    j = 1
    while 6 ** j <= n:
        tmp6_pre = tmp6
        tmp6[6 ** j:] = dp[:-6 ** j] + 1
        tmp6 = np.minimum(tmp6_pre, tmp6)
        j += 1
    k = 1
    while 9 ** k <= n:
        tmp9_pre = tmp9
        tmp9[9 ** k:] = dp[:-9 ** k] + 1
        tmp9 = np.minimum(tmp9_pre, tmp9)
        k += 1
    tmp1 = np.minimum(tmp1, tmp6)
    tmp1 = np.minimum(tmp1, tmp9)
    dp = np.minimum(dp, tmp1)
    loop += 1
print(dp[n])
