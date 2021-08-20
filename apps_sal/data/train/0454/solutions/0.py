class Solution:

    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        nums = [int(_) for _ in s]
        dp = [-1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                dp[i] = i
            else:
                dp[i] = i if nums[i] > nums[dp[i + 1]] else dp[i + 1]
        for i in range(len(nums)):
            if nums[i] != nums[dp[i]]:
                (nums[i], nums[dp[i]]) = (nums[dp[i]], nums[i])
                break
        res = 0
        for num in nums:
            res = res * 10 + num
        return res
