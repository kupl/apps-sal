import sys
import math
import collections
import bisect
import itertools
import fractions
import copy
import heapq
import decimal
import queue
INF = 10 ** 16
MOD = 998244353


def ni():
    return int(sys.stdin.readline())


def ns():
    return list(map(int, sys.stdin.readline().split()))


def na():
    return list(map(int, sys.stdin.readline().split()))


class ModCombination:

    def __init__(self, maxN, MOD):
        self._maxN = maxN
        self._MOD = MOD
        self.facts = [1]
        self.invs = [1] * (self._maxN + 1)
        fact = 1
        for i in range(1, self._maxN + 1):
            fact *= i
            fact %= self._MOD
            self.facts.append(fact)
        inv = pow(fact, self._MOD - 2, self._MOD)
        self.invs[self._maxN] = inv
        for i in range(self._maxN, 1, -1):
            inv *= i
            inv %= self._MOD
            self.invs[i - 1] = inv

    def nCr(self, n, r):
        return self.facts[n] * self.invs[r] * self.invs[n - r] % self._MOD


def main():
    (n, m, k) = ns()
    mc = ModCombination(n, MOD)
    result = 0
    for ki in range(k + 1):
        ans = 1
        ans *= m % MOD
        ans *= pow(m - 1, n - 1 - ki, MOD)
        ans %= MOD
        ans *= mc.nCr(n - 1, ki)
        ans %= MOD
        result += ans
        result %= MOD
    print(result)


def __starting_point():
    main()


__starting_point()
