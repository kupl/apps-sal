def main():
    n = int(input())
    limit = int(n ** .5) + 1
    lim12 = max(limit, 12)
    lim = lim12 // 6
    l = [False, True, True] * lim
    lim = lim * 3 - 1
    for i, s in enumerate(l):
        if s:
            p, pp = i * 2 + 3, (i + 3) * i * 2 + 3
            le = (lim - pp) // p + 1
            if le > 0:
                l[pp::p] = [False] * le
            else:
                break
    l[3] = True
    primes = [i for i, s in zip(list(range(3, lim12, 2)), l) if s]
    for i, p in enumerate((3, 5, 7)):
        primes[i] = p
    res = False
    for x in n, n - 2, n - 4:
        if x > primes[-1]:
            for p in primes:
                if not x % p:
                    break
            else:
                res = True
        else:
            res = x in primes
        if res:
            print((n - x) // 2 + 1)
            print(x, *([2] * ((n - x) // 2)))
            return
    l, cache = [], set()
    for b in primes:
        l.append(b)
        for c in l:
            a = n - b - c
            if a not in cache:
                for p in primes:
                    if not a % p:
                        cache.add(a)
                        break
                else:
                    print(3)
                    print(a, b, c)
                    return


def __starting_point():
    main()


__starting_point()
