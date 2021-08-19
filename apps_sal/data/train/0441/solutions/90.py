import math


class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        i = 1
        count = 0
        while i < math.ceil((math.sqrt(1 + 8 * N) + 1) / 2):
            if (2 * N - i * i + i) % (2 * i) == 0:
                count += 1
            i += 1
        return count
