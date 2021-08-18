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


r1, c1, r2, c2 = map(int, input().split())
MOD = 10**9 + 7
ans = 0

ans += getComb(r2 + c2 + 2, r2 + 1, MOD)
ans -= getComb(r2 + c1 + 1, r2 + 1, MOD)
ans -= getComb(r1 + c2 + 1, r1, MOD)
ans += getComb(r1 + c1, r1, MOD)

print(ans % MOD)
