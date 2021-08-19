(N, M) = list(map(int, input().split()))
'nを素因数分解'
'2以上の整数n => [[素因数, 指数], ...]の2次元リスト'


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


a = prime_factorize(N)
b = prime_factorize(M)
c = set(a) & set(b)
print(len(c) + 1)
