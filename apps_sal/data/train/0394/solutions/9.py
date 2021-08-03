class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        med = sorted(nums)[len(nums) // 2]
        return sum([abs(num - med) for num in nums])
