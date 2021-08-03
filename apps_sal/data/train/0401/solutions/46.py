class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]

        for n in nums:
            for i in dp[:]:
                dp[(i + n) % 3] = max(dp[(i + n) % 3], i + n)

        return dp[0]
