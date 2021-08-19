from bisect import bisect_left


def genprimes(limit):
    lim = limit // 6
    sieve = [False, True, True] * lim
    lim = lim * 3 - 1
    for (i, s) in enumerate(sieve):
        if s:
            (p, pp) = (i * 2 + 3, (i + 3) * i * 2 + 3)
            le = (lim - pp) // p + 1
            if le > 0:
                sieve[pp::p] = [False] * le
            else:
                break
    sieve[0] = sieve[3] = True
    res = [i * 2 + 3 for (i, f) in enumerate(sieve) if f]
    res[:4] = [2, 3, 5, 7]
    return res


def main():
    primes = genprimes(100004)
    (n, m) = list(map(int, input().split()))
    res = [0] * m
    for y in range(n):
        rw = 0
        for (x, z) in enumerate(map(int, input().split())):
            p = primes[bisect_left(primes, z)] - z
            res[x] += p
            rw += p
        res.append(rw)
    print(min(res))


def __starting_point():
    main()


__starting_point()
