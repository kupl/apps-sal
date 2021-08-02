import sys
import math


def get_sum(a, d, n):
    return ((2 * a + (n - 1) * d) * n) >> 1


def main():
    n = int(input())

    divisors = set()
    for d in range(1, min(n + 1, 10**5)):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)

    fun_values = [get_sum(1, d, n // d) for d in divisors]
    fun_values = sorted(list(fun_values))

    print(' '.join(str(v) for v in fun_values))


def __starting_point():
    main()


__starting_point()
