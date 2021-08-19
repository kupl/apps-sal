class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        m = {0: 0}
        for (i, pre) in enumerate(itertools.accumulate(nums)):
            if pre - target in m:
                dp[i + 1] = max(dp[i], dp[m[pre - target]] + 1)
            else:
                dp[i + 1] = dp[i]
            m[pre] = i + 1
        return dp[-1]
