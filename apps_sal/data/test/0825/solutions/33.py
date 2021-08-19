n = int(input())


def prime_factorize(n):
    n_origin = n + 0
    primelist = []
    a = 2
    while a * a <= n_origin:
        if n % a != 0:
            a += 1
            continue
        ex = 0
        while n % a == 0:
            ex += 1
            n = n // a
        primelist.append([a, ex])
        a += 1
    if n != 1:
        primelist.append([n, 1])
    return primelist


def sumf(n):
    return n * (n + 1) // 2


primes = prime_factorize(n)
ans = 0
for pl in primes:
    (a, ex) = pl
    i = 0
    while True:
        if sumf(i + 1) > ex:
            break
        i += 1
    ans += i
print(ans)
