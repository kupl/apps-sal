class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set(nums)
        a = sum(a) * 3 - sum(nums)
        return int(a / 2)
