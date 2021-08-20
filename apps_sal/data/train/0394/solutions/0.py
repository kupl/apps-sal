class Solution:

    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        aa = sorted(nums)
        median = aa[len(nums) // 2]
        return sum([abs(i - median) for i in aa])
