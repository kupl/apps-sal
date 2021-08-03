x, n = input().split(' ')
x, n = int(x), int(n)

primes = []

for i in range(2, 100000):
    if x % i == 0:
        primes.append(i)
        while x % i == 0:
            x = x // i

if x != 1:
    primes.append(x)

result_list = []
MOD = 1000000007

for p in primes:
    result = 0
    pk = p
    while pk <= n:
        result += n // pk
        pk *= p
    result_list.append((result, p))


def power(a, b):
    nonlocal MOD
    if b == 0:
        return 1
    r = 1
    ak = a
    while b > 0:
        if b % 2 == 1:
            r *= ak
        b = b // 2
        ak *= ak
        ak %= MOD
        r %= MOD
    return r


result = 1
for r, p in result_list:
    result *= power(p, r)
    result %= MOD


print(result)
