N, K = [int(_) for _ in input().split()]
mod = 10**9 + 7
A = [0] * (K + 1)
for i in range(K, 0, -1):
    A[i] = pow(K // i, N, mod)
    for j in range(2, K // i + 1):
        A[i] -= A[i * j]
        A[i] %= mod
print((sum(i * a for i, a in enumerate(A)) % mod))

