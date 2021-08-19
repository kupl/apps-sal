class Solution:

    def minDifference(self, nums: List[int]) -> int:
        return min((b - a for (a, b) in zip(sorted(nums)[:4], sorted(nums)[-4:])))
