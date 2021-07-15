import sys
mod = 10 ** 6 + 3

n, k = list(map(int, input().split()))

if n < 100:
    if 2 ** n < k:
        print(1, 1)
        return

def factor(n, p):
    if n < p: return 0
    return n // p + factor(n // p, p)

def inv(n):
    return pow(n, mod - 2, mod)

# 2^nk - P(2^n,k) / 2^nk

two = inv(pow(2, n + factor(k - 1, 2), mod))

v = 1

if k >= mod:
    v = 0
else:
    N = pow(2, n, mod)
    for i in range(k):
        v = v * (N - i) % mod

A = (pow(2, n * k, mod) - v) * two % mod
B = pow(2, n * k, mod) * two % mod

print(A, B)

