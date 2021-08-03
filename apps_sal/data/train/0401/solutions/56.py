class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for num in nums:
            for prev in dp[:]:
                dp[(prev + num) % 3] = max(prev + num, dp[(prev + num) % 3])
        return dp[0]
