from collections import deque
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        step = 0
        while len(nums):
            for i, val in enumerate(nums):
                if val % 2:
                    nums[i] -= 1
                    step += 1
            nums = self.trim(nums)
            if len(nums):
                step += 1
                for i, val in enumerate(nums):
                    if val:
                        nums[i] /= 2
            nums = self.trim(nums)
        return step

    def trim(self, nums):
        return [e for e in nums if e]

