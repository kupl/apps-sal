# coding:UTF-8
import sys
from math import factorial

MOD = 10 ** 9 + 7

# 二項係数 順列　組み合わせ


def combInit(n):
    fact = [1]
    finv = [1]
    for i in range(1, n + 1):
        fact.append(fact[i - 1] * i % MOD)
        finv.append(pow(fact[i], MOD - 2, MOD))
    return [fact, finv]


def comb(n, k, f):
    if n < k:
        return 0
    elif n < 0 or k < 0:
        return 0
    else:
        return f[0][n] * (f[1][k] * f[1][n - k] % MOD) % MOD


N = int(input())    # 数字
caa = input()
cab = input()
cba = input()
cbb = input()

f = combInit(1000)

if N <= 3:
    print((1))
    return

if cab == "A":
    if caa == "A":
        res = 1
    elif caa == "B":
        if cba == "A":
            res = 1
            for i in range(1, (N - 2) // 2 + 1):
                nt = N - 2 - i
                t = comb(nt, i, f)
                res = (res + t) % MOD
        elif cba == "B":
            res = pow(2, N - 3, MOD)
elif cab == "B":
    if cbb == "B":
        res = 1
    elif cbb == "A":
        if cba == "B":
            res = 1
            for i in range(1, (N - 2) // 2 + 1):
                nt = N - 2 - i
                t = comb(nt, i, f)
                res = (res + t) % MOD
        elif cba == "A":
            res = pow(2, N - 3, MOD)

print(("{}".format(res)))
