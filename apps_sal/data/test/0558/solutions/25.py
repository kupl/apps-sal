
N, M, K = list(map(int, input().rstrip().split()))
fact = [0] * (N + 1)
fact_inv = [0] * (N + 1)
inv = [0] * (N + 1)

mod = 998244353

fact[0] = fact[1] = 1
fact_inv[0] = fact_inv[1] = 1
inv[1] = 1

for i in range(2, N + 1):
    fact[i] = (fact[i - 1] * i) % mod
    inv[i] = mod - (inv[mod % i] * (mod // i)) % mod
    fact_inv[i] = (fact_inv[i - 1] * inv[i]) % mod

pow_M1 = [0] * N
pow_M1[0] = 1

for i in range(1, N):
    pow_M1[i] = (pow_M1[i - 1] * (M - 1)) % mod

ans = 0

for i in range(K + 1):
    comb = (fact[N - 1] * fact_inv[i] * fact_inv[N - 1 - i]) % mod

    ans += (comb * M * pow_M1[N - i - 1]) % mod
    ans %= mod

print(ans)
