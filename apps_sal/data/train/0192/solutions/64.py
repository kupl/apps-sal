from functools import cmp_to_key


def cmp(a, b):
    return b - a


class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(key=cmp_to_key(cmp))
        tot = 0
        i = 1
        N = len(piles)
        n = int(N / 3)
        for i in range(1, N - n + 1, 2):
            tot += piles[i]
        return tot
