import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
mod = 10**9 + 7
N, M = map(int, readline().split())

fact = [1] * (M + 1)
fact_inv = [1] * (M + 1)
for i in range(1, M + 1):
    fact[i] = fact[i - 1] * i % mod
fact_inv[M] = pow(fact[M], mod - 2, mod)
for i in range(M, 0, -1):
    fact_inv[i - 1] = (i * fact_inv[i]) % mod


def comb(n, r):
    return fact[n] * fact_inv[r] * fact_inv[n - r] % mod


total = 0
for k in range(N + 1):
    a = fact[M - k] * fact_inv[M - N] * comb(N, k) % mod
    if k % 2 == 0:
        total += a
    else:
        total -= a
ans = (comb(M, N) * fact[N]) % mod * total
print(ans % mod)
