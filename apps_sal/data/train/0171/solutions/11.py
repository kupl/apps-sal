class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[nums[0], nums[0]] for _ in range(n)]
        ans = nums[0]
        for i in range(1, n):
            temp = [dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i]]
            dp[i][0], dp[i][1] = max(temp), min(temp)
            if dp[i][0] > ans:
                ans = dp[i][0]
        return ans

#        n = len(nums)
#        dp = [[nums[0], nums[0]]] * n   尽量不要使用乘法
#        ans = nums[0]
#        for i in range(1, n):
#            temp = [dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i]]
#            dp[i][0], dp[i][1] = max(temp), min(temp)   这样赋值会改变所有值
#            if dp[i][0] > ans:
#                ans = dp[i][0]
#        return dp[-1][0]
