from collections import Counter


def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    fct = Counter(fct)
    return fct


mod = 10**9 + 7


def comb_mod(n, r, mod):
    ans = 1
    for i in range(r):
        ans *= n - i
        ans %= mod
    for i in range(1, r + 1):
        ans *= pow(i, mod - 2, mod)
        ans %= mod
    return ans


N, M = map(int, input().split())
fact = factorize(M)
ans = 1
for k in fact.values():
    ans *= comb_mod(k + N - 1, k, mod)
    ans %= mod
print(ans)
