MOD = 10**9 + 7
fac = [1 for k in range(200010)]
inv = [1 for k in range(200010)]
finv = [1 for k in range(200010)]
for k in range(2, 200010):
    fac[k] = (fac[k - 1] * k) % MOD
    inv[k] = (MOD - inv[MOD % k] * (MOD // k)) % MOD
    finv[k] = (finv[k - 1] * inv[k]) % MOD


def nCr(n, r):
    return (fac[n] * finv[r] * finv[n - r]) % MOD


H, W, A, B = list(map(int, input().split()))
ans = 0

for k in range(W - B):
    ans += nCr(A + W - B - k - 2, A - 1) * nCr(B + k + 1 + H - A - 2, H - A - 1)
    ans %= MOD

print(ans)
