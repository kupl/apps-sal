class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if not days:
            return 0
        dp = {}

        def getMin(idx, valid_count_past):
            if idx == len(days):
                return 0
            if days[idx] <= valid_count_past:
                return getMin(idx + 1, valid_count_past)
            if idx in dp:
                return dp[idx]
            m1 = costs[0] + getMin(idx + 1, days[idx])
            m7 = costs[1] + getMin(idx + 1, days[idx] + 6)
            m30 = costs[2] + getMin(idx + 1, days[idx] + 29)
            dp[idx] = min(m1, m7, m30)
            return dp[idx]

        return getMin(0, 0)
