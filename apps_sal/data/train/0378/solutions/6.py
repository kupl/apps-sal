class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = 0
        bits = 1

        for num in nums:
            s += num
            bits |= bits << num

        return not (s & 1) and ((bits >> (s >> 1)) & 1) == 1
