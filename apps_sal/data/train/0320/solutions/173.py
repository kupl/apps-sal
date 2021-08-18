

from collections import deque


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        step = 0
        while sum(nums):
            for i, val in enumerate(nums):
                if val % 2:
                    nums[i] -= 1
                    step += 1
            if sum(nums):
                step += 1
                for i, val in enumerate(nums):
                    if val:
                        nums[i] /= 2
        return step
