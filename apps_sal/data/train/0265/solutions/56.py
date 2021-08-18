class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        presum = 0

        last_pos = {0: 0}
        dp = [0] * (1 + n)
        for i in range(1, 1 + n):
            presum += nums[i - 1]
            dp[i] = dp[i - 1]
            if presum - target in last_pos:
                pos = last_pos[presum - target]
                dp[i] = max(dp[i], dp[pos] + 1)
            last_pos[presum] = i
        return dp[n]
