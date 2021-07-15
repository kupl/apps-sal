N, K = list(map(int, input().split()))
MOD = 10**9 + 7
MAX_N = 10**6 + 5
fact = [0]*(MAX_N)
fact_inv = [0]*(MAX_N)
fact[0] = 1
for i in range(MAX_N-1):
    fact[i+1] = fact[i]*(i+1) % MOD
fact_inv[-1] = pow(fact[-1], MOD-2, MOD)
for i in range(MAX_N-2, -1, -1):
    fact_inv[i] = fact_inv[i+1]*(i+1) % MOD


def comb(n, k):
    return fact[n]*fact_inv[k] % MOD * fact_inv[n-k] % MOD


if K >= N:
    print((comb(2*N-1, N-1)))
    return

ans = 1
for i in range(1, K+1):
    ans += comb(N, i)*comb(N-1, i) % MOD
    ans %= MOD
print(ans)

