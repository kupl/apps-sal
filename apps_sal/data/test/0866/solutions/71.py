X, Y = map(int, input().split())
n = (2 * X - Y) // 3
m = (-X + 2 * Y) // 3
if n < 0 or m < 0 or (2 * X - Y) % 3 != 0 or (-X + 2 * Y) % 3 != 0:
    print(0)
else:
    # (n+m)Cn 通り
    fac = [1, 1]
    finv = [1, 1]
    inv = [1, 1]
    MOD = 10 ** 9 + 7
    for i in range(2, n + m + 1):
        fac.append(fac[i - 1] * i % MOD)
        inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
        finv.append(finv[i - 1] * inv[i] % MOD)
    
    print(fac[n+m] * (finv[n] * finv[m] % MOD) % MOD)
