def isPrime(n):
    def compositeTry(a, d, n, s):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n - 1:
                return False
        return True

    knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    if n in knownPrimes:
        return True
    if any((n % p) == 0 for p in knownPrimes) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    return not any(compositeTry(a, d, n, s) for a in (2, 3, 5, 7))


def main():
    n = int(input())
    if isPrime(n):
        print((1))
    elif n % 2 == 0:
        print(2)
    elif isPrime(n - 2):
        print(2)
    else:
        print(3)


main()
