from math import gcd
(N, K) = list(map(int, input().split()))
mod = 10 ** 9 + 7
A = [0] * K
for i in range(K, 0, -1):
    a = K // i
    b = pow(a, N, mod)
    A[i - 1] = b
for i in range(K, 0, -1):
    for j in range(K // i - 1):
        c = i * (j + 2)
        A[i - 1] -= A[c - 1]
        A[i - 1] %= mod
s = 0
for i in range(K):
    s += A[i] * (i + 1)
    s %= mod
print(s)
