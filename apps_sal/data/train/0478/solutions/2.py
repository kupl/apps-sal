class Solution:

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        (ones, twos) = (0, 0)
        for i in nums:
            ones = ones ^ i & ~twos
            twos = twos ^ i & ~ones
        return ones
