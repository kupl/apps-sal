'''h2d5
ポイントは重複組み合わせ（仕切りと中身）と素因数因数分解
N+素因数分解の指数-1から指数を選ぶ組み合わせ（指数-1が仕切りの枚数）
nPr=n!/(n-r)!   
nCr=n!/(n-r)!*r!=(n*(n-1)*...*(n-r+1))/r!(分子分母は共にｒ個)
'''
import math
MOD = 10**9 + 7


def comb(n, r):
    nPr = 1
    fact_r = 1
    for i in range(r):
        nPr *= n - i
        fact_r *= r - i
    return nPr // fact_r


N, M = map(int, input().split())
fact = {}
for i in range(2, int(math.sqrt(M)) + 1):
    if M == 1:
        break
    while(M % i == 0):
        M //= i
        if not i in fact:
            fact[i] = 1
        else:
            fact[i] += 1
if M != 1:
    fact[M] = 1

answer = 1
for r in fact.values():
    answer *= comb(N + r - 1, r)
    answer %= MOD

print(answer)
