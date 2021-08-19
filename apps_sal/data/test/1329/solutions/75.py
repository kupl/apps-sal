from math import sqrt


def sieve(n):
    if n <= 4:
        return list(range(2, n))

    def _sieve_of_eratosthenes(n):
        limit = int(sqrt(n)) + 1
        (*table,) = [1] * n
        table[0] = table[1] = 0
        for i in range(2, limit):
            if table[i]:
                for j in range(i ** 2, n, i):
                    table[j] = 0
        return [i for i in range(2, n) if table[i]]
    return _sieve_of_eratosthenes(n)


def factorint(n):
    d = {}
    for i in range(2, int(sqrt(n)) + 1):
        c = 0
        (q, r) = divmod(n, i)
        while not r:
            c += 1
            n = q
            (q, r) = divmod(n, i)
        if c:
            d[i] = c
    if n != 1:
        d[n] = 1
    return d


n = int(input())
P = sieve(n + 1)
d = {p: i for (i, p) in enumerate(P)}
X = [1] * len(P)
for i in range(2, n + 1):
    for (k, v) in factorint(i).items():
        X[d[k]] += v
nb_3 = len([x for x in X if x >= 3])
nb_5 = len([x for x in X if x >= 5])
nb_15 = len([x for x in X if x >= 15])
nb_25 = len([x for x in X if x >= 25])
nb_75 = len([x for x in X if x >= 75])
print(nb_75 + nb_25 * (nb_3 - 1) + nb_15 * (nb_5 - 1) + nb_5 * (nb_5 - 1) * (nb_3 - 2) // 2)
