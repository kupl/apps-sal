MOD = 10 ** 9 + 7
fac = [1 for k in range(200010)]
inv = [1 for k in range(200010)]
finv = [1 for k in range(200010)]
for k in range(2, 200010):
    fac[k] = fac[k - 1] * k % MOD
    inv[k] = (MOD - inv[MOD % k] * (MOD // k)) % MOD
    finv[k] = finv[k - 1] * inv[k] % MOD


def nCr(n, r):
    return fac[n] * finv[r] * finv[n - r] % MOD


(N, K) = list(map(int, input().split()))
A = sorted(list(map(int, input().split())))
m = 0
for k in range(N - K + 1):
    m += A[k] * nCr(N - k - 1, K - 1)
    m %= MOD
A = A[::-1]
M = 0
for k in range(N - K + 1):
    M += A[k] * nCr(N - k - 1, K - 1)
    M %= MOD
print(M - m if M >= m else M - m + MOD)
