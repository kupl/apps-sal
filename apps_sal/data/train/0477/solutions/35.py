import math


class Solution:

    def findKthBit(self, j: int, k: int) -> str:
        n = j
        lst = ['0']
        for i in range(n):
            lst = lst + ['1'] + ['1' if ele == '0' else '0' for ele in lst[::-1]]
        return lst[k - 1]
