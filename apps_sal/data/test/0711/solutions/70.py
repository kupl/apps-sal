from collections import Counter
from scipy.special import comb
(n, m) = list(map(int, input().split()))
mod = 10 ** 9 + 7


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


c = Counter(prime_factorize(m))
ans = 1
for (key, value) in list(c.items()):
    ans *= comb(value + n - 1, value, exact=True) % mod
print(ans % mod)
