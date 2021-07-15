from math import log2, log
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0

        def op0() -> int:
            nonlocal nums
            ops = sum([n % 2 for n in nums])
            nums = [((n >> 1) << 1) for n in nums]
            return ops

        def op1() -> int:
            nonlocal nums
            ops = 0
            while sum([n % 2 for n in nums]) == 0:
                ops += 1
                nums = [n // 2 for n in nums]
            return ops

        # print(nums)
        while sum(nums):
            ops += op0()
            # print(f\"op0: {nums}, ops={ops}\")
            if sum(nums):
                ops += op1()
                # print(f\"op1: {nums}, ops={ops}\")

        return ops
