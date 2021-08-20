class Solution:
    """
    days = [1,4,6,7,8,20]
    dp   = 11 9 8 6 4  2
            2 7        2
    """

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        for i in range(1, -1, -1):
            if costs[i] > costs[i + 1]:
                costs[i] = costs[i + 1]
        N = len(days)
        dp = [0 for _ in range(N + 1)]
        dp[-2] = costs[0]
        dp[-1] = 0
        for i in range(N - 2, -1, -1):
            dp[i] = costs[0] + dp[i + 1]
            for j in range(i + 1, N):
                if days[j] - days[i] < 7:
                    dp[i] = min(dp[i], costs[1] + dp[j + 1])
                elif days[j] - days[i] < 30:
                    dp[i] = min(dp[i], costs[2] + dp[j + 1])
        return dp[0]
