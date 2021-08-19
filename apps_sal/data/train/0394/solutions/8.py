class Solution:

    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '\n         nums = sorted(nums)\n         N = len(nums)\n         if N%2 == 1:\n             medium = nums[N//2]\n             steps = [abs(x-medium) for x in nums]\n             return sum(steps)\n         else:\n             medium = (nums[N//2-1]+nums[N//2])/2\n             steps = [abs(x-medium) for x in nums]\n             return int(sum(steps))'
        length = len(nums)
        nums = sorted(nums)
        median = nums[length // 2]
        steps = [abs(x - median) for x in nums]
        return sum(steps)
