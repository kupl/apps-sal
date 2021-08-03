class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)

        n = len(nums)
        dp = [0 for i in range(n + 1)]

        temp = {0: 0}
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if preSum[i] - target in temp:
                dp[i] = max(dp[i], dp[temp[preSum[i] - target]] + 1)
            temp[preSum[i]] = i

        return dp[n]
