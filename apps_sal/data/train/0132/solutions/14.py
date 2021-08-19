from collections import defaultdict


class Solution:

    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        dp = defaultdict(int)
        days = set(days)
        for i in range(365, 0, -1):
            if i in days:
                dp[i] = min(dp[i + 1] + cost[0], dp[i + 7] + cost[1], dp[i + 30] + cost[2])
            else:
                dp[i] = dp[i + 1]
        return dp[1]
