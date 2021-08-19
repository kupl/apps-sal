class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0] + [-float('inf')] * (5000 + target)
        for i in range(1, target + 1):
            for (j, c) in enumerate(cost):
                dp[i] = max(dp[i], 10 * dp[i - c] + j + 1)
        print(dp[:target + 1])
        return str(max(dp[target], 0))
    '  \n    def largestNumber(self, cost, target):\n        dp = [0] + [-1] * (target + 5000)\n        for t in xrange(1, target + 1):\n            dp[t] = max(dp[t - c] * 10 + i + 1 for i, c in enumerate(cost))\n        return str(max(dp[t], 0))\n    '
