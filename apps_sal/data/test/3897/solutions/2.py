from math import sqrt, factorial as f
from collections import Counter
from operator import mul
from functools import reduce


def comb(n, m):
    o = n - m
    if m and o:
        if m < o:
            m, o = o, m
        return reduce(mul, list(range(m + 1, n)), n) // f(o)
    return 1


def main():
    n = int(input())
    aa = list(map(int, input().split()))
    if n == 1:
        print(1)
        return
    lim = int(sqrt(max(aa)) // 6) + 12
    sieve = [False, True, True] * lim
    lim = lim * 3 - 1
    for i, s in enumerate(sieve):
        if s:
            p, pp = i * 2 + 3, (i + 3) * i * 2 + 3
            le = (lim - pp) // p + 1
            if le > 0:
                sieve[pp::p] = [False] * le
            else:
                break
    sieve[0] = sieve[3] = True
    primes = [i * 2 + 3 for i, f in enumerate(sieve) if f]
    for i, p in enumerate((2, 3, 5, 7)):
        primes[i] = p
    del sieve
    c = Counter()
    for x in aa:
        for p in primes:
            cnt = 0
            while not x % p:
                x //= p
                cnt += 1
            if cnt:
                c[p] += cnt
                if x == 1:
                    break
        if x > 1:
            c[x] += 1
    x, inf = 1, 1000000007
    for p, cnt in list(c.items()):
        x = x * comb(cnt + n - 1, n - 1) % inf
    print(x)


def __starting_point():
    main()


__starting_point()
