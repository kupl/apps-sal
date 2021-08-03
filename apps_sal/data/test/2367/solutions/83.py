def combmod_pre(N, p):
    '''
    sample usage:
        p = 10**9+7
        N = 10**6
        fact, finv = combmod_pre(N, p)
        combmod(n, r, p)
    '''
    fact = [1, 1]
    finv = [1, 1]
    inv = [0, 1]
    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        finv.append((finv[-1] * inv[-1]) % p)
    return (fact, finv)


def combmod(n, r, fact, finv, p):
    '''
    sample usage:
        combmod(3000, 1000, fact, finv, p)
            p is a same value of combmod_pre's argument
            fact, finv is return value of combmod_pre
    '''
    if r < 0 or n < r:
        return 0
    return fact[n] * finv[r] * finv[n - r] % p


p = 10**9 + 7
N = 10**6
fact, finv = combmod_pre(N, p)

h, w, a, b = (int(x) for x in input().split())
ans = 0
for j in range(b, w):
    x = combmod(h - a - 1 + j, j, fact, finv, p)
    y = combmod(a + w - 2 - j, w - 1 - j, fact, finv, p)
    ans += x * y
print((ans % p))
