class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        ln = len(nums)
        ret = 0
        sums = {0: 0}
        dp = [0] * (ln + 1)
        s = 0
        for i in range(ln):
            s += nums[i]
            if s - target in sums:
                idx = sums[s - target]
                dp[i + 1] = 1 + dp[idx]
            dp[i + 1] = max(dp[i], dp[i + 1])
            sums[s] = i + 1
        return dp[ln]
        pass
