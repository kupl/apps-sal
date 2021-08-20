import numpy as np
MOD = 998244353
(n, s) = map(int, input().split())
a = list(map(int, input().split()))
fac_inv2 = pow(2, MOD - 2, MOD)
dp = np.zeros(s, 'int64')
for i in range(n):
    newdp = dp.copy()
    if a[i] < s:
        newdp[a[i]:] += dp[:s - a[i]] * fac_inv2 % MOD
    if a[i] <= s:
        newdp[a[i] - 1] += 1
    dp = newdp % MOD
ans = dp[-1]
ans *= pow(2, n - 1, MOD)
ans %= MOD
print(ans)
