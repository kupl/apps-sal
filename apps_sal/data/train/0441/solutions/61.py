import math


class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        k = 1.0
        count = 0
        while k <= math.sqrt(2 * N + 1 / 4) - 1 / 2:
            x = N / k - (k + 1) / 2
            if x.is_integer():
                count += 1
            k += 1
        return count
