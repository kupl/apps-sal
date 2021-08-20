import numpy as np
import sys
input = sys.stdin.readline
MOD = 998244353
(n, s) = map(int, input().split())
A = list(map(int, input().split()))
F = np.zeros(s + 1, dtype=np.int64)
ans = 0
for a in A:
    F[0] += 1
    F[a:] += F[:-a].copy()
    F %= MOD
    ans += F[s]
    ans %= MOD
print(ans)
