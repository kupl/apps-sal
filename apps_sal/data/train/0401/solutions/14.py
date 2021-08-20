class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0, 0, 0]] * (len(nums) + 1)
        for i in range(len(nums)):
            cand = dp[i] + [n + nums[i] for n in dp[i]]
            for c in cand:
                j = c % 3
                dp[i + 1][j] = max(dp[i + 1][j], c)
        return dp[-1][0]
