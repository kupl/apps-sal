import math
import sys
from collections import Counter
MOD = 1000000007


def f(a, b):
    ret = 0
    pow10 = 1
    while a and b:
        ret += b % 10 * pow10
        pow10 *= 10
        b //= 10
        ret += a % 10 * pow10
        pow10 *= 10
        a //= 10
    ret += a * pow10
    ret += b * pow10
    return ret


def ndigits(a):
    ret = 0
    while a:
        ret += 1
        a //= 10
    return ret


def contrib_for_digs(x, part_digs, x_is_a):
    partner = 10 ** (part_digs - 1)
    (a1, b1) = (partner, x)
    (a2, b2) = (2 * partner, x)
    if x_is_a:
        (a1, b1) = (b1, a1)
        (a2, b2) = (b2, a2)
    return 2 * f(a1, b1) - f(a2, b2)


def contrib(a, cnt):
    ret = 0
    for (part_digs, part_cnt) in list(cnt.items()):
        ret += part_cnt * contrib_for_digs(a, part_digs, True)
        ret += part_cnt * contrib_for_digs(a, part_digs, False)
    return ret


def solve_case():
    n = int(input())
    a = [int(p) for p in input().split()]
    a.sort()
    digs = [ndigits(ai) for ai in a]
    cnt = Counter(digs)
    ret = 0
    for ai in a:
        ret += contrib(ai, cnt)
    print(ret % 998244353)


if __name__ == '__main__' and (not hasattr(sys, 'ps1')):
    solve_case()
