def main():
    n = int(input())
    primes = dict()
    ans = 1
    for i in range(2, n + 1):
        t = i
        j = 2
        while j * j <= t:
            k = 0
            while t % j == 0:
                t //= j
                k += 1
            if k != 0:
                if j in primes:
                    primes[j] = max(primes[j], k)
                else:
                    primes[j] = k
            j += 1
        if t != 1:
            if t in primes:
                primes[t] = max(primes[t], 1)
            else:
                primes[t] = 1
    for (i, t) in list(primes.items()):
        ans *= i ** t
    print(ans + 1)


def __starting_point():
    main()


__starting_point()
