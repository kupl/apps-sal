import math
(a, b) = map(int, input().split())
g = math.gcd(a, b)
'\ngを素因数分解したときの素因数のリストの要素数 + 「1」を含める\n\ng == 1のとき\n1\ng != 1のとき\n素因数リストの要素数 +1\n'


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
if gdlist == []:
    print(1)
else:
    print(len(set(gdlist)) + 1)
