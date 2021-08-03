class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[-math.inf] * 3 for _ in nums]
        dp[0][nums[0] % 3] = nums[0]
        for i, n in enumerate(nums[1:], start=1):
            dp[i][n % 3] = n
            for j in range(3):
                dp[i][j] = max(dp[i][j], dp[i - 1][j], n + dp[i - 1][(j - n % 3) % 3])
        ans = dp[-1][0]
        return ans if ans > 0 else 0
