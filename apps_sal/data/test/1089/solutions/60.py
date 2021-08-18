
def comb(n, k, mod):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    k = min(n - k, k)
    ans = 1
    inv = [1] * (k + 1)
    if k >= 1:
        ans *= (n - k + 1) % mod
    for i in range(2, k + 1):
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        ans = ans * (n - k + i) * inv[i] % mod
    return ans


n, m, k = map(int, input().split())

MOD = 1000000007

distX = 0
for d in range(n):
    distX += d * (n - d) * m ** 2

distY = 0
for d in range(m):
    distY += d * (m - d) * n ** 2

ans = ((distX + distY) * comb(n * m - 2, k - 2, MOD)) % MOD

print(ans)
