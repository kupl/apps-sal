from math import factorial
n, m = list(map(int, input().split()))
if abs(n - m) > 1:
    print((0))
    return
mod = 10**9 + 7
if n == m:
    print(((2 * factorial(n) * factorial(m)) % mod))
else:
    print(((factorial(n) * factorial(m)) % mod))
