import math


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        for n in range(1, math.ceil(-0.5 + math.sqrt(0.25 + 2 * N))):
            start = N / (n + 1) - n / 2
            if math.isclose(0, start - math.floor(start)):
                count += 1
        return count + 1
