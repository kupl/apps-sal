from heapq import nsmallest
from math import inf as _inf
import sys as _sys


def main():
    n, = _read_ints()
    a = tuple(_read_ints())
    result = find_max_power_can_make(a)
    print(result)


def _read_line():
    result = _sys.stdin.readline()
    assert result[-1] == "\n"
    return result[:-1]


def _read_ints():
    return map(int, _read_line().split())


def find_max_power_can_make(heroes_powers):
    heroes_powers = tuple(heroes_powers)
    assert heroes_powers

    abs_powers_sum = sum(map(abs, heroes_powers))

    if len(heroes_powers) <= 9:
        return _compute_using_brute_force(heroes_powers)

    zeros_n = heroes_powers.count(0)
    if zeros_n >= 2:
        return abs_powers_sum
    assert zeros_n <= 1

    n = len(heroes_powers)
    if n % 3 == 1 % 3:
        can_invert_mod_3 = 0
    elif n % 3 == 2 % 3:
        can_invert_mod_3 = 2
    else:
        assert n % 3 == 3 % 3
        can_invert_mod_3 = 1

    result = -_inf

    for is_zero_positive in (False, True):

        if zeros_n == 0 or is_zero_positive:
            signs = [1 if x >= 0 else -1 for x in heroes_powers]
        else:
            signs = [1 if x > 0 else -1 for x in heroes_powers]

        negative_n = signs.count(-1)
        have_pair_of_same = any(signs[i] == signs[i + 1] for i in range(len(signs) - 1))
        is_trivial = not (not have_pair_of_same and negative_n % 3 == can_invert_mod_3)

        if is_trivial:
            if negative_n % 3 == can_invert_mod_3:
                result = max(result, abs_powers_sum)
                continue
            negative_to_inverse_1 = negative_n
            while negative_to_inverse_1 % 3 != can_invert_mod_3:
                negative_to_inverse_1 -= 1
            negative_to_inverse_2 = negative_to_inverse_1 + 3
        else:
            negative_to_inverse_1 = negative_n - 3
            negative_to_inverse_2 = negative_n + 3
            min_pos = max(
                heroes_powers,
                key=lambda x: (x >= 0 if is_zero_positive else x > 0, -abs(x))
            )
            max_neg = max(
                heroes_powers,
                key=lambda x: (x < 0 if is_zero_positive else x <= 0, x)
            )
            result = max(result, abs_powers_sum - 2 * abs(min_pos) - 2 * abs(max_neg))

        if negative_to_inverse_1 >= 0:
            negative_to_remain_n = negative_n - negative_to_inverse_1
            assert negative_to_remain_n > 0
            negative_powers = tuple(filter(
                lambda x: x < 0 if is_zero_positive else x <= 0, heroes_powers
            ))
            if negative_to_remain_n <= len(negative_powers):
                negative_to_remain = nsmallest(
                    negative_to_remain_n, negative_powers, key=abs
                )
                result = max(result, abs_powers_sum - 2 * abs(sum(negative_to_remain)))

        if negative_to_inverse_2 <= n:
            positive_to_inverse_n = negative_to_inverse_2 - negative_n
            assert positive_to_inverse_n > 0
            positive_powers = tuple(filter(
                lambda x: x >= 0 if is_zero_positive else x > 0, heroes_powers
            ))
            if positive_to_inverse_n <= len(positive_powers):
                positive_to_inverse = nsmallest(
                    positive_to_inverse_n, positive_powers, key=abs
                )
                result = max(result, abs_powers_sum - 2 * sum(positive_to_inverse))

    return result


def _compute_using_brute_force(seq):
    n = len(seq)
    if n == 1:
        return seq[0]
    return max(
        _compute_using_brute_force(seq[:i] + (-(seq[i] + seq[i + 1]),) + seq[i + 2:])
        for i in range(n - 1)
    )


def __starting_point():
    main()


__starting_point()
