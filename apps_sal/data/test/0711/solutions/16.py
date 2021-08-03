import sys
import collections

input = sys.stdin.readline


def modInverse(a, p):
    return pow(a, p - 2, p)


def modBinomial(n, k, p):
    numerator = 1
    for i in range(k):
        numerator = (numerator * (n - i)) % p

    denominator = 1
    for i in range(1, k + 1):
        denominator = (denominator * i) % p

    return (numerator * modInverse(denominator, p)) % p


def main():
    N, M = [int(x) for x in input().split()]

    MOD = 10 ** 9 + 7

    def prime_factorization(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    x = prime_factorization(M)

    c = collections.Counter(x)

    ans = 1
    for k in list(c.keys()):
        ans *= modBinomial(c[k] + N - 1, c[k], MOD)

    print((ans % MOD))


def __starting_point():
    main()


__starting_point()
