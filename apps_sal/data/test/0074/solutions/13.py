def main():
    n = int(input())
    limit = int(n ** 0.5) + 1
    lim12 = max(limit, 12)
    lim = lim12 // 6
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
    sieve[3] = True
    primes = [i for (i, s) in zip(list(range(3, lim12, 2)), sieve) if s]
    for (i, p) in enumerate((3, 5, 7)):
        primes[i] = p
    while primes and primes[-1] >= limit:
        del primes[-1]
    for x in (n, n - 2, n - 4):
        for p in primes:
            if not x % p:
                break
        else:
            print((n - x) // 2 + 1)
            print(x, *[2] * ((n - x) // 2))
            return
    for a in range(n // 2 | 1, n, 2):
        for p in primes:
            if not a % p:
                break
        else:
            for c in primes:
                b = n - a - c
                if b < 3:
                    break
                for p in primes:
                    if not b % p:
                        break
                else:
                    print(3)
                    print(a, b, c)
                    return


def __starting_point():
    main()


__starting_point()
