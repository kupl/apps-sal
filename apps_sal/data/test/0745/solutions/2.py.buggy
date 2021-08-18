MOD = 998244353
fac = [1] * (2 * 10 ** 5 + 10)


def comb(n, k):
    return fac[n] * pow(fac[n - k], MOD - 2, MOD) * pow(fac[k], MOD - 2, MOD) % MOD


for i in range(len(fac) - 1):
    fac[i + 1] = fac[i] * (i + 1) % MOD
n, k = list(map(int, input().split()))
if k == 0:
    print(fac[n])
else:
    k = n - k
    if k <= 0:
        print(0)
        return
    ans = 0
    for i in range(k + 1):
        t = comb(k, i) * pow(k - i, n, MOD) % MOD
        if i % 2:
            ans -= t
        else:
            ans += t
    print(2 * ans * comb(n, k) % MOD)
