MOD = 10 ** 9 + 7
MAX = 2 * 10 ** 5
fac = [1, 1] + [0] * MAX
finv = [1, 1] + [0] * MAX
inv = [0, 1] + [0] * MAX
for i in range(2, MAX + 2):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = -inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD


def comb(n, r):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n - r] % MOD) % MOD


(H, W, A, B) = list(map(int, input().split()))
ans = 0
for i in range(1, H - A + 1):
    cnt = comb(i - 1 + B - 1, i - 1)
    cnt *= comb(H - i + W - B - 1, H - i)
    ans += cnt
    ans %= MOD
print(ans)
