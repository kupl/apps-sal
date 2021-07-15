import copy


def prepare(n, MOD):
 
    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
     
    return factorials, invs

def func(r, c):
    return f[r+1+c+1] * i[r+1] % MOD * i[c+1] % MOD

MOD = 10**9+7
f, i = prepare(2*10**6 + 2, MOD)


r1, c1, r2, c2 = map(int,input().split())

combi = func(r2, c2) - func(r2, c1-1) - func(r1-1, c2) + func(r1-1, c1-1)
print(combi % MOD)   
