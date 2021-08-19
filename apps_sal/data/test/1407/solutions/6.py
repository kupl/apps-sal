from bisect import bisect_left


def sieve(r):
    D = dict()
    yield 2
    for q in range(3, r, 2):
        p = D.pop(q, None)
        if not p:
            D[q * q] = q
            yield q
        else:
            x = p + q
            while x in D or not x & 1:
                x += p
            D[x] = p


primes = list(sieve(1000003))


def II():
    return list(map(int, input().split()))


(n, m) = II()
grid = [[primes[bisect_left(primes, x)] - x for x in II()] for _ in range(n)]
print(min(min((sum(row) for row in grid)), min((sum(col) for col in zip(*grid)))))
