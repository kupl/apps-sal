n, a, b = map(int, input().split())


def fact(n, p):
    a = 1
    for i in range(1, n + 1):
        a = (a * i) % p
    return a


def bfact(n, x, p):
    a = 1
    for i in range(n - x + 1, n + 1):
        a = (a * i) % p
    return a


p = 10**9 + 7
na = bfact(n, a, p) % p
nb = bfact(n, b, p) % p
aa = fact(a, p) % p
bb = fact(b, p) % p
aaa = pow(aa, -1, p)
bbb = pow(bb, -1, p)
ans = pow(2, n, p) - 1
ans -= (na * aaa + nb * bbb)
print(ans % p)
