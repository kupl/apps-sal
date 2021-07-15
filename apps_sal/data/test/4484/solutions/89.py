import math

n, m = map(int, input().split())
n_f = math.factorial(n)
m_f = math.factorial(m)
mod = 1000000007

if abs(n-m) > 1:
    print(0)
    return
if n == m:
    print((n_f * m_f * 2) % mod)
else:
    print((n_f * m_f) % mod)
