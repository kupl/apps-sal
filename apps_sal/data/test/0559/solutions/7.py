import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18


def get_factorials(max, mod=None):
    """
    階乗 0!, 1!, 2!, ..., max!
    :param int max:
    :param int mod:
    :return:
    """
    ret = [1]
    n = 1
    if mod:
        for i in range(1, max + 1):
            n *= i
            n %= mod
            ret.append(n)
    else:
        for i in range(1, max + 1):
            n *= i
            ret.append(n)
    return ret


def mod_invs(max, mod):
    """
    逆元のリスト 0 から max まで
    :param int max:
    :param int mod:
    """
    invs = [1] * (max + 1)
    for x in range(2, max + 1):
        invs[x] = (-(mod // x) * invs[mod % x]) % mod
    return invs


def factorial_invs(max, mod):
    """
    階乗 0!, 1!, 2!, ..., max! の逆元
    :param int max:
    :param int mod:
    """
    ret = []
    r = 1
    for inv in mod_invs(max, mod):
        r = r * inv % mod
        ret.append(r)
    return ret


class Combination:
    def __init__(self, max, mod):
        """
        :param int max:
        :param int mod: 3 以上の素数であること
        """
        self._factorials = get_factorials(max, mod)
        self._finvs = factorial_invs(max, mod)
        self._mod = mod

    def ncr(self, n, r):
        """
        :param int n:
        :param int r:
        :rtype: int
        """
        if n < r:
            return 0
        return (
            self._factorials[n] *
            self._finvs[r]
            % self._mod *
            self._finvs[n - r]
            % self._mod
        )


P = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))


def power_table():
    ret = np.ones((P, P), dtype=int)
    row = -np.arange(P, dtype=int)
    for i in range(1, P):
        ret[i] = ret[i - 1] * row % P
    return ret


comb = Combination(max=P - 1, mod=P)
ncr = np.array([comb.ncr(P - 1, i) for i in range(P)])
power = power_table()

B = np.zeros(P, dtype=int)
for j, a in enumerate(A):
    if a == 0:
        continue
    B -= power[:, j] * ncr % P
    B[-1] += 1
    B %= P
print((*B[::-1]))
