class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for num in nums:
            for x in dp[:]:
                dp[(x + num) % 3] = max(dp[(x + num) % 3], x + num)
        return dp[0]
