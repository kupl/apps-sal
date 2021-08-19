class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        csum = {}
        csum[0] = 0
        dp = [0 for i in range(len(nums) + 1)]
        (sum, best) = (0, 0)
        for (i, v) in enumerate(nums):
            sum += v
            x = sum - target
            dp[i + 1] = dp[i]
            if x in csum:
                dp[i + 1] = max(dp[i + 1], dp[csum[x]] + 1)
            best = max(best, dp[i + 1])
            csum[sum] = i + 1
        return best
