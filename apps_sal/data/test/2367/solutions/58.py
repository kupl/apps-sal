LIMIT = 2 * 10 ** 5
fac = [0] * (LIMIT + 10)
fac[0] = 1
inv = [0] * (LIMIT + 10)
MOD = 1_000_000_007
n = 1
for i in range(1, LIMIT + 1):
    n *= i
    n %= MOD
    fac[i] = n
inv[LIMIT] = pow(fac[LIMIT], MOD - 2, MOD)
for i in range(LIMIT, -1, -1):
    inv[i - 1] = (inv[i] * i) % MOD
def C(n, r):
    return (fac[n] * inv[n-r] * inv[r]) % MOD

H, W, A, B = list(map(int, input().split()))
ans = 0
B1 = B - 1
WB1 = W - B - 1
for i in range(H - A):
    ans += C(i + B1, B1) * C(H - i - 1 + WB1, WB1)
    ans %= MOD
print(ans)

