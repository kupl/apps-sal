class Solution:

    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        return min((x - y for (x, y) in zip(nums[-4:], nums[:4])))
