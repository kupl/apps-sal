import sys
from collections import defaultdict

input = sys.stdin.readline


def calc_prime_factors(n, count=False):
    """Trial division"""
    factors = []
    # factor: 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # factor: 3, 5, 7, 11, ...
    f = 3
    root_n = int(n ** 0.5) + 1
    while f <= root_n:
        if n % f == 0:
            factors.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        factors.append(n)
    return factors


def main():
    N = int(input())

    n_factor = defaultdict(int)
    for n in range(1, N + 1):
        factors = calc_prime_factors(n)
        for f in factors:
            n_factor[f] += 1

    n_factor = list(n_factor.values())
    n_factor.sort()
    ans = 0

    # 75 = 3 x 3 x 5 : (2, 4, 4)
    A, B = 0, 0
    for n in n_factor:
        if 2 <= n <= 3:
            A += 1
        elif 4 <= n:
            B += 1
    ans += A * B * (B - 1) // 2 + B * (B - 1) * (B - 2) // 6 * 3

    # 75 = 3 x 25 : (2, 24)
    A, B = 0, 0
    for n in n_factor:
        if 2 <= n <= 23:
            A += 1
        elif 24 <= n:
            B += 1
    ans += A * B + B * (B - 1)

    # 75 = 5 x 15 : (4, 14)
    A, B = 0, 0
    for n in n_factor:
        if 4 <= n <= 13:
            A += 1
        elif 14 <= n:
            B += 1
    ans += A * B + B * (B - 1)

    # 75 = 75 : (74,)
    A = 0
    for n in n_factor:
        if 74 <= n:
            A += 1
    ans += A

    print(ans)


def __starting_point():
    main()

__starting_point()
