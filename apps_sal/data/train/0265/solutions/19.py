class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        res = 0
        seen = {}
        used_i = 0
        nums = [0] + nums
        for (i, num) in enumerate(nums):
            if num - target in seen and seen[num - target] >= used_i:
                res += 1
                used_i = i
            seen[num] = i
        return res
