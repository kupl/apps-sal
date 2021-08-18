class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        mins = [-1 for i in range(len(nums))]
        mins[0] = nums[0]

        for i in range(1, len(nums)):
            mins[i] = min(mins[i - 1], nums[i])
        s = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != mins[i]:
                while s and s[-1] <= mins[i]:
                    s.pop()
                if s and s[-1] < nums[i]:
                    return True
                s.append(nums[i])
        return False
