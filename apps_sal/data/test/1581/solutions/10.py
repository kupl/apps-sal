import numpy as np
import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7
(n, k) = map(int, input().split())
S = set()
i = 1
while i * i <= n:
    S.add(i)
    S.add(n // i)
    i += 1
L = np.array([0] + sorted(S), dtype=np.int64)
l = len(L) - 1
num = np.diff(L)
dp = np.zeros(l, dtype=np.int64)
dp[0] = 1
for _ in range(k):
    A = np.cumsum(dp)
    dp = A[::-1] * num
    dp %= MOD
ans = dp.sum() % MOD
print(ans)
