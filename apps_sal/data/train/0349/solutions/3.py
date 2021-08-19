class Solution:

    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        upper = max(nums)
        ordered = [0] * (upper + 1)
        for i in nums:
            ordered[i] += i
        ans = [0] * (upper + 1)
        ans[1] = ordered[1]
        for i in range(2, upper + 1):
            ans[i] = max(ans[i - 1], ans[i - 2] + ordered[i])
        return ans[upper]
