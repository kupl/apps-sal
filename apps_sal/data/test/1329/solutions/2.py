def make_prime_table(n):
    sieve = list(range(n + 1))
    sieve[0] = -1
    sieve[1] = -1
    for i in range(4, n + 1, 2):
        sieve[i] = 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i] != i:
            continue
        for j in range(i * i, n + 1, i * 2):
            if sieve[j] == j:
                sieve[j] = i
    return sieve


def prime_factorize(n):
    result = []
    while n != 1:
        p = prime_table[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        result.append((p, e))
    return result


N = int(input())
prime_table = make_prime_table(N)
d = {}
for i in range(2, N + 1):
    for (p, e) in prime_factorize(i):
        d.setdefault(p, 0)
        d[p] += e
n74 = 0
n24 = 0
n14 = 0
n4 = 0
n2 = 0
for k in d:
    if d[k] >= 74:
        n74 += 1
    if d[k] >= 24:
        n24 += 1
    if d[k] >= 14:
        n14 += 1
    if d[k] >= 4:
        n4 += 1
    if d[k] >= 2:
        n2 += 1
result = 0
result += n4 * (n4 - 1) // 2 * (n2 - 2)
result += n14 * (n4 - 1)
result += n24 * (n2 - 1)
result += n74
print(result)
