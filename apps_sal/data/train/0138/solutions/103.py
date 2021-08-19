class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        """
        f(i, 0) +
        f(i, 1) -
        f(i, 0) = max(f(i-1, 0)*nums[i]>0, f(i-1, 1), nums[i] < 0)
        f(i, 1) = 
        """
        dp = defaultdict(int)
        for (i, num) in enumerate(nums):
            if num > 0:
                dp[i, 0] = 1
            if num < 0:
                dp[i, 1] = 1
        ans = dp[0, 0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp[i, 0] = max(dp[i, 0], dp[i - 1, 0] + 1 if dp[i - 1, 0] > 0 else 0)
                dp[i, 1] = max(dp[i, 1], dp[i - 1, 1] + 1 if dp[i - 1, 1] > 0 else 0)
            if nums[i] < 0:
                dp[i, 0] = max(dp[i, 0], dp[i - 1, 1] + 1 if dp[i - 1, 1] > 0 else 0)
                dp[i, 1] = max(dp[i, 1], dp[i - 1, 0] + 1 if dp[i - 1, 0] > 0 else 0)
            ans = max(ans, dp[i, 0])
        return ans
