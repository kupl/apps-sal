class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0] + [float('-inf')] * target
        for i in range(9, 0, -1):
            for j in range(1, target + 1):
                if j >= cost[i - 1]:
                    dp[j] = max(dp[j], (dp[j - cost[i - 1]] * 10) + i)
        return str(dp[target]) if dp[target] > 0 else '0'
