import numpy as np


class Solution:

    def minOperations(self, n: int) -> int:
        res = 0
        for i in range(n):
            value = 2 * i + 1 - n
            if value > 0:
                res += value
        return res
