class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) <= 1:
            return False
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == 0 and nums[i - 1] == 0:
                    return True
        else:
            nums[0] = nums[0] % k
            for i in range(1, len(nums)):
                nums[i] = (nums[i - 1] + nums[i]) % k
                if nums[i] == 0:
                    return True
            numdict = {}
            for i in range(len(nums)):
                if nums[i] not in numdict:
                    numdict[nums[i]] = i
                elif i > numdict[nums[i]] + 1:
                    return True
        return False
