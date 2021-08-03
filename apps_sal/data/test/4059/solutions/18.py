# -*- coding: utf-8 -*-


def run_prime_factorization(max_number: int) -> dict:
    '''Run prime factorization.
    Args:
        max_number: Int of number (greater than 1).
    Returns:
        A dictionary's items ((base, exponent) pairs).
    Landau notation: O(log n)
    '''

    from math import sqrt

    ans = dict()
    remain = max_number

    for base in range(2, int(sqrt(max_number)) + 1):
        if remain % base == 0:
            exponent_count = 0

            while remain % base == 0:
                exponent_count += 1
                remain //= base

            ans[base] = exponent_count

    if remain != 1:
        ans[remain] = 1

    return ans


def main():
    from math import floor
    import sys
    input = sys.stdin.readline

    n = int(input())
    ans = 0

    for a in range(1, n):
        b = floor(n / a)
        ans += b

    p = list(run_prime_factorization(n).values())

    if len(p) == 1:
        ans -= list(p)[0]
    else:
        count = 1

        for pi in p:
            count *= (pi + 1)

        ans -= count
        ans += 1

    print(ans)


def __starting_point():
    main()


__starting_point()
