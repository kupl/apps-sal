from math import factorial
mod = 10 ** 9 + 7
(n, m) = map(int, input().split())
print((factorial(n) % mod) ** 2 % mod * 2 % mod if n == m else factorial(n) % mod * (factorial(m) % mod) % mod if abs(n - m) == 1 else 0)
