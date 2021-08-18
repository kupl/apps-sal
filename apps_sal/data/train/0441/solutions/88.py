

class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        def consum(p):
            return p * (p + 1) / 2

        count = 0
        i = 1
        while consum(i) <= N:
            if (N - consum(i)) % i == 0:
                count += 1
            i += 1
        return count
