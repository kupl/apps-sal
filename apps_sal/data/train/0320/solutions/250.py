from typing import Tuple


class Solution:
    def ones_twos(self, n: int, ones: int, twos: int) -> Tuple[int, int]:
        if n == 0:
            return ones, twos
        if n == 1:
            return ones + 1, twos
        if n % 2 == 0:
            return self.ones_twos(n // 2, ones, twos + 1)
        else:
            return self.ones_twos(n - 1, ones + 1, twos)

    def minOperations(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            o, t = self.ones_twos(num, 0, 0)
            ones += o
            twos = max(twos, t)
        return ones + twos
