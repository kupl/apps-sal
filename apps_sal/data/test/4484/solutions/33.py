import sys
import math

mod = 10**9 + 7
N, M = map(int, sys.stdin.readline().split())
diff = abs(N - M)
if diff > 1:
    print(0)
    return

n_p = 1
for i in range(1, N + 1):
    n_p *= i
    n_p %= mod
m_p = 1
for i in range(1, M + 1):
    m_p *= i
    m_p %= mod

if diff == 0:
    print(2 * n_p * m_p % mod)
else:
    print(n_p * m_p % mod)
