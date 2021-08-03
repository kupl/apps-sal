class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
         nums = sorted(nums)
         N = len(nums)
         if N%2 == 1:
             medium = nums[N//2]
             steps = [abs(x-medium) for x in nums]
             return sum(steps)
         else:
             medium = (nums[N//2-1]+nums[N//2])/2
             steps = [abs(x-medium) for x in nums]
             return int(sum(steps))"""

        length = len(nums)
        nums = sorted(nums)
        median = nums[length // 2]
        steps = [abs(x - median) for x in nums]
        return sum(steps)
