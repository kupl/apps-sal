from math import factorial
x, y = list(map(int, input().split()))
mod = 10**9 + 7

if (2 * y - x) % 3 != 0 or (2 * x - y) % 3 != 0:
    print((0))
    return
s = (2 * x - y) // 3
t = (2 * y - x) // 3


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = mod
N = 10 ** 6 + 1  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans = cmb(s + t, s, p)
print(ans)
