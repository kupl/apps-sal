class Solution:

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l_nums = len(nums)
        c = 0
        state = dict()
        state[0] = 1
        sum = 0
        for idx in range(0, l_nums):
            sum += nums[idx]
            if sum - k in state:
                c += state[sum - k]
            state[sum] = (state[sum] if sum in state else 0) + 1
        return c
