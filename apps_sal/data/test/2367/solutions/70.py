# -*- coding: utf-8 -*-
# コンビネーション
def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod


N = 2 * 10 ** 5 + 1000  # N は必要分だけ用意する
mod = pow(10, 9) + 7
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

ans = 0
h, w, a, b = list(map(int, input().split()))
for i in range(h - a):
    #print(b - 1 + i, i, w - b - 1 + h - i - 1, w - b - 1)
    ans += (cmb(b - 1 + i, i) * cmb(w - b - 1 + h - i - 1, w - b - 1)) % (10 ** 9 + 7)
print((ans % (10 ** 9 + 7)))
