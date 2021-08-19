# -*- coding: utf-8 -*-
# nCをp(=10**9+7)で割ったときのあまり(モジュラ逆数)
def cmb(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return facto[n] * factoinv[r] * factoinv[n - r] % p


p = 10**9 + 7
n, m = map(int, input().split())
# 0,1の時の値をいれたn!のリスト(modp)
facto = [1, 1]
# 0,1の時の値をいれたn!の逆元のリスト(modp)
factoinv = [1, 1]
# 0,1の場合を入れたn!の逆元も求めるために使うnの逆元のリスト(modp)
inv = [0, 1]
# 2からスタート
for i in range(2, m + 1):
    facto.append((facto[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factoinv.append((factoinv[-1] * inv[-1]) % p)
if n == m:
    kosuub = 0
    for i in range(n + 1):
        kosuub += (facto[(n - i)] * cmb(n, i, p) * ((-1)**i)) % p
    kosuu = (kosuub * facto[(n)]) % p
    print(kosuu)
else:
    kosuub = 0
    for i in range(n + 1):
        kosuub += (cmb((m - i), (n - i), p) * facto[(n - i)] * cmb(n, i, p) * ((-1)**i)) % p
    kosuu = (kosuub * cmb(m, n, p) * facto[n]) % p
    print(kosuu)
