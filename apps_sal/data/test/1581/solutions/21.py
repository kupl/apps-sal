import numpy as np

n, k = list(map(int, input().split()))
MOD = 10 ** 9 + 7
l = int(n ** 0.5)
coe = [n // i - l for i in range(l, 0, -1)]
coe.append(0)
coe.reverse()
coe = np.array(coe, dtype=np.int64)

dp1 = np.ones(l + 1, dtype=np.int64)
dp2 = coe.copy()
dp1[0] = 0
for i in range(k - 1):
    dp1acc_f = np.add.accumulate(dp1) % MOD
    dp1acc_b = np.add.accumulate((dp1 * coe % MOD)[::-1])[::-1] % MOD
    s = dp1acc_f[-1]
    dp1acc_f = np.roll(dp1acc_f, 1)
    dp1[1:] = (s + dp2[1:]) % MOD
    dp2[1:] = (dp1acc_b + dp1acc_f * coe)[1:] % MOD
ans = (dp1.sum() + dp2[1]) % MOD
print(ans)

