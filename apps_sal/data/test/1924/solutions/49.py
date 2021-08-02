r1, c1, r2, c2 = map(int, input().split())

MOD = 10 ** 9 + 7
N = r2 + c2 + 10
fact = [0 for _ in range(N)]
invfact = [0 for _ in range(N)]
fact[0] = 1
for i in range(1, N):
    fact[i] = fact[i - 1] * i % MOD

invfact[N - 1] = pow(fact[N - 1], MOD - 2, MOD)

for i in range(N - 2, -1, -1):
    invfact[i] = invfact[i + 1] * (i + 1) % MOD


def nCk(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return fact[n] * invfact[k] * invfact[n - k] % MOD


ans = nCk(r2 + c2 + 2, r2 + 1) - nCk(r2 + c1 + 1, r2 + 1) \
    - nCk(r1 + c2 + 1, c2 + 1) + nCk(r1 + c1, r1)
print(ans % MOD)
