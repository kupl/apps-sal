(k, n) = map(int, input().split())
mod = 998244353
max_n = 5000
(fac, finv, inv) = ([0] * max_n, [0] * max_n, [0] * max_n)


def comInit(max_n):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, max_n):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod


comInit(max_n)


def com(n, k):
    if n < k:
        return 0
    if (n < 0) | (k < 0):
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


ex2 = [1] * 1010
for i in range(1, 1010):
    ex2[i] = ex2[i - 1] * 2 % mod
ans = []
for j in range(2, k + 2):
    tmp = 0
    x = (j - 1) // 2
    for i in range(j // 2 + 1):
        comb1 = com(n + k - j, n - i)
        comb2 = com(x, i) * ex2[i] % mod
        if j % 2 == 0:
            comb1 += com(n + k - j - 1, n - i - 1)
            comb1 %= mod
        tmp += comb1 * comb2
        tmp %= mod
    ans.append(tmp)
ans2 = ans[:-1]
ans += ans2[::-1]
print('\n'.join(map(str, ans)))
