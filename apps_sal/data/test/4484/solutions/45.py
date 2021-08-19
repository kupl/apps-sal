from math import factorial as f
(n, m) = list(map(int, input().split()))
mod = 10 ** 9 + 7
if abs(n - m) == 1:
    res = f(n) * f(m)
    print(res % mod)
elif n == m:
    res = f(n) * f(m) * 2
    print(res % mod)
else:
    print(0)
