def make_prime_table(N):
    sieve = list(range(N + 1))
    sieve[0] = -1
    sieve[1] = -1
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i] != i:
            continue
        for j in range(i * i, N + 1, i):
            if sieve[j] == j:
                sieve[j] = i
    return sieve


N = int(input())

prime_table = make_prime_table(100)

d = {}
for i in range(2, N + 1):
    while i != 1:
        d.setdefault(prime_table[i], 0)
        d[prime_table[i]] += 1
        i //= prime_table[i]

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
