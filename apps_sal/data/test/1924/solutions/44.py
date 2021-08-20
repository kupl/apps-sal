import sys
read = sys.stdin.read
mod = 10 ** 9 + 7
(r1, c1, r2, c2) = map(int, read().split())


def prepare(n, MOD):
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return (factorials, invs)


(fac, finv) = prepare(2 * 10 ** 6 + 10, mod)


def comb(n, k, mod=mod, fac=fac, finv=finv):
    """
    二項係数の計算

    Parameters
    n : int
        元集合
    k : int
        元集合から選択する数
    mod : int
        あまり
    fac : list
        階乗のリスト
    finv : list
        逆元のリスト

    Returns
    c : int
        nCkの組み合わせの数
    """
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


answer = comb(r2 + c2 + 2, r2 + 1) - comb(r1 + c2 + 1, r1) - comb(c1 + r2 + 1, c1) + comb(r1 + c1, r1)
answer %= mod
print(answer)
