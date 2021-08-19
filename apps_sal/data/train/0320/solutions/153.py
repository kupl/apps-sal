from functools import lru_cache


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        divideByTwos = 0
        decrements = 0
        for num in nums:
            if num == 0:
                continue
            (divides, dec) = self.reductions(num)
            divideByTwos = max(divideByTwos, divides)
            decrements += dec
        return divideByTwos + decrements

    @lru_cache(maxsize=None)
    def reductions(self, num: int) -> (int, int):
        decrements = 0
        divides = 0
        while num > 1:
            if num % 2 == 0:
                num /= 2
                divides += 1
            else:
                num -= 1
                decrements += 1
        return (divides, decrements + 1)
