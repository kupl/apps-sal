class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        pos = {0: -1}
        n = len(nums)
        dp = [0] * (n + 1)
        s = 0
        for i in range(n):
            s += nums[i]
            dp[i + 1] = dp[i]
            t = s - target
            if t in pos:
                dp[i + 1] = max(dp[i + 1], dp[pos[t] + 1] + 1)
            pos[s] = i
        return dp[-1]
