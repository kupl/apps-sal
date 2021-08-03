MOD = 10**9 + 7

N, M, K = list(map(int, input().split()))


def getComb(n, k, MOD):
    if n < k:
        return 0
    if n - k < k:
        k = n - k
    comb = 1
    for x in range(n - k + 1, n + 1):
        comb = (comb * x) % MOD
    d = 1
    for x in range(1, k + 1):
        d = (d * x) % MOD
    comb *= pow(d, MOD - 2, MOD)
    return comb % MOD


comb = getComb(N * M - 2, K - 2, MOD)

ans = 0
for i in range(N):
    ans += i * (N - i) * M * M
    ans %= MOD

for j in range(M):
    ans += j * (M - j) * N * N
    ans %= MOD

ans *= comb
ans %= MOD

print(ans)
