import numpy as np
(n, k) = list(map(int, input().split()))
MOD = 10 ** 9 + 7
l = int(n ** 0.5)
coe = []
for i in range(l, 0, -1):
    coe.append(n // i - l)
coe.append(0)
coe.reverse()
coe = np.array(coe, dtype=np.int64)
dp1 = np.ones(l + 1, dtype=np.int64)
dp2 = coe.copy()
dp1[0] = 0
for i in range(k - 1):
    dp1acc = np.add.accumulate(dp1) % MOD
    dp12acc = np.add.accumulate((dp1 * coe % MOD)[::-1])[::-1]
    s = dp1acc[-1]
    dp1acc = np.roll(dp1acc, 1)
    dp1acc[0] = 0
    dp12acc[0] = 0
    dp1[1:] = (s + dp2[1:]) % MOD
    dp2 = dp12acc + dp1acc * coe % MOD
ans = (dp1.sum() + dp2[1]) % MOD
print(ans)
