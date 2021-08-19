class Solution:

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        nums.append(0)
        for i in reversed(range(len(nums))):
            n = nums[i]
            while n >= 0 and n < len(nums) and (i != n):
                (nums[n], nums[i]) = (nums[i], nums[n])
                if n == nums[i]:
                    break
                n = nums[i]
        print(nums)
        for (i, n) in enumerate(nums):
            if i == 0:
                continue
            if i != n:
                return i
        return nums[-1] + 1
