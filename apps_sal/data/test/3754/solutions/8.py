MOD = 998244353

N = int(input())
ds = list(map(int, input().split()))

sigma_d = 0
pi_d = 1
for d in ds:
    sigma_d += d
    sigma_d %= MOD
    pi_d *= d
    pi_d %= MOD

# perm : (sigma_d-n) P (N-2)
perm = 1
for i in range(N - 2):
    perm *= (sigma_d - N - i)
    perm %= MOD

print((perm * pi_d % MOD))


