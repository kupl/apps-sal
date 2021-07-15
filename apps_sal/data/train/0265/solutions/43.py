class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        seen = {0: 0}
        res = 0
        for i, n in enumerate(nums):
            if n-target in seen:
                res += 1
                seen = {n:0}
            else:
                seen[n] = i
        return res
