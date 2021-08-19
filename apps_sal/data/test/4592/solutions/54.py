import collections
n = int(input())
t = 1
for i in range(1, n + 1):
    t *= i


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


c = collections.Counter(prime_factorize(t))
ans = 1
for (_, v) in c.items():
    ans *= v + 1
print(ans % (10 ** 9 + 7))
