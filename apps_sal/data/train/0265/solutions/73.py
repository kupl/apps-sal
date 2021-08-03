class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        cur = 0
        n = len(nums)
        dp = [0] * (n + 1)
        dic = {}
        dic[0] = 0

        for i in range(1, n + 1):
            cur += nums[i - 1]
            if cur - target in dic:
                dp[i] = 1 + dp[dic[cur - target]]
            dp[i] = max(dp[i], dp[i - 1])

            dic[cur] = i

        return dp[n]
