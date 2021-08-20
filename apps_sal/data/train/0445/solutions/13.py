class Solution:

    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        l = [y - x for (x, y) in zip(nums[:4], nums[-4:])]
        return min(l)
