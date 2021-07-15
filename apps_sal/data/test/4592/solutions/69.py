from collections import Counter
from math import factorial
N = int(input())
MOD = 10 ** 9 + 7

def prime(n):
    b = 2
    while b * b <= n:
        while n % b == 0:
            n //= b
            a.append(b)
        b += 1
    if n > 1:
        a.append(n)

a = []
prime(factorial(N))
A = Counter(a)
X = 1
for k, v in A.items():
    X *= (v + 1) % MOD
print(X % MOD)
