import math
import itertools
import operator


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
          31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
          73, 79, 83, 89, 97]


def get_prime_mult(n):
    m = [0] * 25
    if n < 2:
        return m
    sq = int(math.sqrt(n))
    p = 0
    while primes[p] <= sq:
        if n % primes[p] != 0:
            p += 1
        else:
            m[p] += 1
            n //= primes[p]
            sq = int(math.sqrt(n))

    m[primes.index(n)] += 1
    return m


a, b, c = list(map(int, input().split()))
mtab = []
for i in range(max((a, b, c)) + 1):
    mtab.append(get_prime_mult(i))

total = 0
mults_cnt = {}
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            if i * j * k not in mults_cnt:
                mults = [sum(triple) + 1 for triple in zip(mtab[i], mtab[j], mtab[k])]
                mults_cnt[i * j * k] = list(itertools.accumulate(mults, operator.mul))[-1]
            total += mults_cnt[i * j * k]

print(total & 0x3FFFFFFF)

