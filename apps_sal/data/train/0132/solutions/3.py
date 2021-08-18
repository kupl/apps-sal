class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        m = len(costs)
        ranges = [1, 7, 30]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                for k in range(j, n + 1):
                    if days[k - 1] - days[j - 1] >= ranges[i - 1]:
                        break
                    dp[k] = min(dp[k], costs[i - 1] + dp[j - 1])
        return dp[n]
