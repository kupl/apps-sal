MOD = 10 ** 9 + 7

n, m, k = map(int, input().split())

MOD = 10 ** 9 + 7
N = n * m + 10
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


ans = 0
for i in range(n - 1, 0, -1):
    ans += m * m * (i + 1) * i // 2
    ans %= MOD
for i in range(m - 1, 0, -1):
    ans += n * n * (i + 1) * i // 2
    ans %= MOD

ans *= nCk(n * m - 2, k - 2)
ans %= MOD
print(ans)
