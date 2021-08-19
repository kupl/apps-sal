from scipy.special import comb, factorial, hyp2f1
from math import log2, floor


def h(k, n):
    return round(2 ** n - 1 - comb(n, k + 1) * hyp2f1(1, k - n + 1, k + 2, -1))


def e(k, n):
    if k == 1:
        return n
    return sum((e(k - 1, j) + 1 for j in range(n)))


class Solution:

    def superEggDrop(self, k: int, n: int) -> int:
        best_case = floor(log2(n) + 1)
        if k >= best_case:
            return best_case
        l = 0
        while e(k, l) < n:
            l += 1
        return l
