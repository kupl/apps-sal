from math import comb


class Solution:

    def numWays(self, s: str) -> int:
        n = len(s)
        k = s.count('1')
        if k % 3:
            return 0
        if k == 0:
            return comb(n - 1, 2) % (10 ** 9 + 7)
        third = k // 3
        start = -1
        for i in range(third):
            start = s.find('1', start + 1)
        first_last = start
        for i in range(third):
            start = s.find('1', start + 1)
        second_last = start
        first_zeros = s.count('0', first_last, s.find('1', first_last + 1))
        second_zeros = s.count('0', second_last, s.find('1', second_last + 1))
        return (first_zeros + 1) * (second_zeros + 1) % (10 ** 9 + 7)
