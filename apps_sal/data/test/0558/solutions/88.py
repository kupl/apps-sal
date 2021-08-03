import sys
import math
import itertools
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**7)
INF = 10**20
MOD = 998244353
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()


def factorialMod(n, p):
    fact = [0] * (n + 1)
    fact[0] = fact[1] = 1
    factinv = [0] * (n + 1)
    factinv[0] = factinv[1] = 1
    inv = [0] * (n + 1)
    inv[1] = 1
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % p
        inv[i] = (-inv[p % i] * (p // i)) % p
        factinv[i] = (factinv[i - 1] * inv[i]) % p
    return fact, factinv


def combMod(n, r, fact, factinv, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


def resolve():
    N, M, K = LI()

    ans = 0
    fact, factinv = factorialMod(N, MOD)

    for i in range(K + 1):
        ans += combMod(N - 1, i, fact, factinv, MOD) * M * pow(M - 1, N - 1 - i, MOD)
        ans %= MOD

    print(ans)


def __starting_point():
    resolve()


__starting_point()
