def calccombi(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


(x, y) = map(int, input().split())
if (x + y) % 3 != 0 or 2 * y < x or 2 * x < y:
    print(0)
else:
    MOD = 1000000007
    n = (2 * y - x) // 3
    m = (2 * x - y) // 3
    fac = [0] * (n + m + 1)
    finv = [0] * (n + m + 1)
    inv = [0] * (n + m + 1)
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2, n + m + 1):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD
    print(calccombi(n + m, n))
