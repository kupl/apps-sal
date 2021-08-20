from scipy.special import comb, factorial, hyp2f1
from math import log2, floor


def h(k, n):
    return round(2 ** n - 1 - comb(n, k + 1) * hyp2f1(1, k - n + 1, k + 2, -1))


def h2(k, n):
    return sum((comb(n, j) for j in range(1, k + 1)))


def fast_sum(k, n):
    c = n
    for i in range(k):
        c *= (n - k) / (k + 1)
    return c


def e(k, n):
    if k == 1:
        return n
    return sum((e(k - 1, j) + 1 for j in range(n)))


class Solution:

    def superEggDrop(self, k: int, n: int) -> int:
        if k == 0:
            return n
        l = 0
        while h2(k, l) < n:
            l += 1
        return l
