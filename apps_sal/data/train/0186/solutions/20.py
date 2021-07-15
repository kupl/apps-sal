class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0] + [-1] * (target + 1)
        for t in range(1, target + 1):
            dp[t] = max(dp[max(t - c, -1)] * 10 + i + 1 for i, c in enumerate(cost))
        return str(max(dp[t], 0))
