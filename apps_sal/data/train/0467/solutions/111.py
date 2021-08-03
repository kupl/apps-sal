import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0
        for i in nums:
            divisor = set()
            for j in range(1, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    divisor.add(j)
                    divisor.add(i // j)
                if len(divisor) > 4:
                    break
            if len(divisor) == 4:
                res += sum(divisor)
        return res
