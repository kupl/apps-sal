class Solution:

    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = sorted(nums)
        count = 0
        for i in snums:
            count += abs(i - snums[int(len(nums) / 2)])
        return count
