class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0] + [-1] * (target + 5000)
        for t in range(1, target + 1):
            for i, c in enumerate(cost):
                dp[t] = max(dp[t], dp[t - c] * 10 + (i + 1))
        return str(max(dp[target], 0))
