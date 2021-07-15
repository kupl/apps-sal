
a,b = map(int,input().split())

import math
g = math.gcd(a,b)

"""
gを素因数分解したときの素因数のリストの要素数 + 「1」を含める

g == 1のとき
1
g != 1のとき
素因数リストの要素数 +1
"""



def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


gdlist = prime_factorize(g)
if gdlist ==[]:
    print(1)
else:
    print(len(set(gdlist))+1)
