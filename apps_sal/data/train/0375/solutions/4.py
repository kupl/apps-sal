class Solution:

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        try:
            return max(list(map(lambda i, j: j - i, nums, nums[1:])))
        except:
            return 0
