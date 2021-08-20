from scipy.special import comb, factorial, hyp2f1
from math import log2, floor


def h(k, n):
    return round(2 ** n - 1 - comb(n, k + 1) * hyp2f1(1, k - n + 1, k + 2, -1))


def h2(k, n):
    return sum((comb(n, j) for j in range(1, k + 1)))


def fast_sum(k, n):
    s = 0
    c = 1
    for i in range(1, k + 1):
        c *= (n - i + 1) / i
        s += c
    return s


def e(k, n):
    if k == 1:
        return n
    return sum((e(k - 1, j) + 1 for j in range(n)))


def f(K, x):
    ans = 0
    r = 1
    for i in range(1, K + 1):
        r *= x - i + 1
        r //= i
        ans += r
    return ans


class Solution:

    def superEggDrop(self, k: int, n: int) -> int:
        if k == 0:
            return n
        l = 0
        while fast_sum(k, l) < n:
            l += 1
        return l
