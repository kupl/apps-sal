from collections import defaultdict
import sys as _sys


def main():
    n, k = _read_ints()
    a = tuple(_read_ints())
    result = find_good_pairs_n(a, k)
    print(result)


def _read_line():
    result = _sys.stdin.readline()
    assert result[-1] == "\n"
    return result[:-1]


def _read_ints():
    return list(map(int, _read_line().split()))


def find_good_pairs_n(sequence, k):
    sequence = tuple(sequence)
    factors_seq = tuple(map(_find_prime_factors, sequence))

    factors_seq = [[(kv[0], kv[1] % k) for kv in list(factors.items())] for factors in factors_seq]
    factors_seq = [[kv for kv in factors if kv[1] > 0] for factors in factors_seq]
    factors_seq = list(map(sorted, factors_seq))
    factors_seq = tuple(map(tuple, factors_seq))

    counter = defaultdict(int)
    for factors in factors_seq:
        counter[factors] += 1

    result = 0
    for factors in factors_seq:
        necessary_factors = tuple((factor, k - amount) for factor, amount in factors)
        result += counter[necessary_factors]
        if factors == necessary_factors:
            result -= 1

    assert result % 2 == 0
    result //= 2
    return result


def _find_prime_factors(x):
    result = dict()

    if x % 2 == 0:
        factor_2_n = 0
        while x & 1 == 0:
            x >>= 1
            factor_2_n += 1
        result[2] = factor_2_n

    factor = 3
    while x != 1 and factor * factor <= x:
        if x % factor == 0:
            factor_n = 0
            while x % factor == 0:
                x //= factor
                factor_n += 1
            result[factor] = factor_n
        factor += 2

    if x != 1:
        result[x] = 1

    return result


def __starting_point():
    main()


__starting_point()
