class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        last_pos = {0: 0}
        dp = [0] * (1 + n)
        for i in range(1, 1 + n):
            dp[i] = dp[i - 1]
            if presum[i] - target in last_pos:
                pos = last_pos[presum[i] - target]
                dp[i] = max(dp[i], dp[pos] + 1)
            last_pos[presum[i]] = i
        return dp[n]
