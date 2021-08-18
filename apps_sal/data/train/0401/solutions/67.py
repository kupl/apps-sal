class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        dp = [0, float('-inf'), float('-inf')]
        for n in nums:
            dp = [max(dp[i], dp[(3 - n % 3 + i) % 3] + n) for i in range(3)]
        return dp[0]
