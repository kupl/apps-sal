class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf') for _ in range(days[-1] + 1)]
        dp[0] = 0
        set_days = set(days)
        for i in range(1, len(dp)):
            if i not in set_days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
        return dp[-1]
