# 素因数分解
import sys
from collections import Counter


def soinsu_bunkai(m):
    pf = {}

    for i in range(2, int(m**0.5) + 1):
        while m % i == 0:
            pf[i] = pf.get(i, 0) + 1
            m //= i
    if m > 1:
        pf[m] = 1
    return pf


# 組み合わせの総数 p=10**9+7 で割ったあまりを求める Satoooh Blog 2020/02/27 4分
"""n<10**7 , p は素数"""


def cmb(n, r, p):

    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


# 初期入力
input = sys.stdin.readline  # 文字列では使わない
mod = 10**9 + 7
p = mod
N, M = map(int, input().split())
a = soinsu_bunkai(M)
ans = 1

n = 10 ** 5 + 100  # n は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

# mod p における n の逆元の計算
for i in range(2, n + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

for i in a.values():
    x = cmb(N + i - 1, i, mod)
    ans *= x
print(ans % mod)
