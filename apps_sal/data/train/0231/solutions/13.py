class Solution:

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1
        for _ in range(10):
            for i in range(len(nums)):
                if i + 1 != nums[i] and 0 < nums[i] <= len(nums):
                    (nums[nums[i] - 1], nums[i]) = (nums[i], nums[nums[i] - 1])
                else:
                    pass
            for i in range(len(nums))[::-1]:
                if i + 1 != nums[i] and 0 < nums[i] <= len(nums):
                    (nums[nums[i] - 1], nums[i]) = (nums[i], nums[nums[i] - 1])
                else:
                    pass
        for i in range(len(nums)):
            if not i + 1 == nums[i]:
                return i + 1
        if sorted(nums) == nums:
            return len(nums) + 1
