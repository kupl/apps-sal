class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0] * 3
        for num in nums:
            tmp = list(dp)
            for s in tmp:
                dp[(s + num) % 3] = max([dp[(s + num) % 3], s + num])
        return dp[0]

