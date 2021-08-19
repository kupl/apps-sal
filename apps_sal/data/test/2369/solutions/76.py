from itertools import accumulate
n, k = map(int, input().split())
As = list(map(int, input().split()))


def modconb(n, mod):
    # テーブルを作る
    fac = [0] * (n + 1)
    finv = [0] * (n + 1)
    inv = [0] * (n + 1)

    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2, n + 1):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
    # 計算
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac, finv


mod = 10**9 + 7
fac, finv = modconb(n, mod)
As.sort()
acc = list(accumulate(As))
As.sort(reverse=True)
acc_r = list(accumulate(As))
ans = 0
for d in range(1, n):
    if d - 1 < k - 2:
        continue
    if k - 2 <= 0:
        c = 1
    else:
        c = fac[d - 1] * (finv[k - 2] * finv[d - 1 - (k - 2)] % mod) % mod
        # c = modconb(d-1,k-2,mod)
    ind = min(d - 1, n - d - 1)
    mn = acc[ind]
    mx = acc_r[ind]
    ans += (mx - mn) * c
    # print(d,c,mn,mx,"d",(mx-mn)*c)
    ans %= mod
print(ans)
