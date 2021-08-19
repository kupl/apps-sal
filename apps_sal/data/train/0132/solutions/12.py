class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        k = len(costs)
        n = len(days)
        dp = [[0] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = float('inf')
            for d in range(i):
                if days[i] - days[d] < 30:
                    dp[i][0] = min(dp[i][0], dp[d][3])
                if days[i] - days[d] < 7:
                    dp[i][0] = min(dp[i][0], dp[d][2])
            for j in range(1, k + 1):
                if i == 0:
                    dp[i][j] = costs[j - 1]
                else:
                    dp[i][j] = costs[j - 1] + min(dp[i - 1])
        return min(dp[-1])
