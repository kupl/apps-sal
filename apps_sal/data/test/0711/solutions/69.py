from collections import Counter
from functools import reduce
import operator
product = lambda it: reduce(operator.mul,it,1)

def comb(n, max_k, mod):
    """
    (n,k) := n個からk個選ぶ組み合わせ
    k = 0~max_Kまでを計算して返す
    """
    res = [1]*(max_k+1)
    t = 1
    for i in range(max_k+1):
        res[i] *= t
        t *= n-i
        t %= mod

    n = reduce(lambda x,y: (x*y)%mod, range(1,max_k+1), 1)
    n = pow(n, mod-2, mod)

    for i in reversed(range(max_k+1)):
        res[i] *= n
        res[i] %= mod
        n *= i
        n %= mod
    return res

# 素因数分解
def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n

MOD = 10**9+7
N,M = map(int,input().split())

factors = Counter(prime_factors(M))

res = 1

for c in factors.values():
    res *= comb(N-1+c,c,MOD)[-1]
    res %= MOD

print(res)
