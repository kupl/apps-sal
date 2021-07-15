MOD = 10**9 + 7
MAX = 2*10**5
fac = [0]*MAX  # fac[n]:  (n!) mod p
finv = [0]*MAX  # finv[n]: (n!)^-1 mod p
inv = [0]*MAX  # inv[n]:  (n)^-1 mod -p


def comb_init():
    nonlocal fac, finv, inv
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD//i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD


def comb(n: int, r: int) -> int:
    nonlocal fac, finv
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n-r] % MOD) % MOD


H, W, A, B = list(map(int, input().split()))
comb_init()
ans = 0

for i in range(H-A):
    x = comb(B-1+i, i)
    a = H-1-i
    b = W-1-B
    x *= comb(a+b, a)
    x %= MOD
    ans += x
ans %= MOD
print(ans)

