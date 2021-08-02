import sys
import math


MAX = 1000010
MOD = 998244353


def main():
    ar = [1 for _ in range(MAX)]
    fact = [1 for _ in range(MAX)]

    for n in range(2, MAX):
        fact[n] = fact[n - 1] * n % MOD

    for n in range(2, MAX):
        ar[n] = ((ar[n - 1] - 1) * n + fact[n]) % MOD

    n = int(input())
    print(ar[n])


def __starting_point():
    main()


__starting_point()
