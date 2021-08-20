MOD = 10 ** 9 + 7


def comb_mod(n, r, mod):
    (a, b) = (1, 1)
    r = min(r, n - r)
    for i in range(r):
        a = a * (n - i) % mod
        b = b * (r - i) % mod
    return a * pow(b, mod - 2, mod) % mod


(N, M, K) = map(int, input().split())
ans = 0
for dx in range(1, M):
    ans += N * N % MOD * (M - dx) % MOD * dx % MOD
    ans %= MOD
for dy in range(1, N):
    ans += M * M % MOD * (N - dy) % MOD * dy % MOD
    ans %= MOD
ans *= comb_mod(N * M - 2, K - 2, MOD)
ans %= MOD
print(ans)
