class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        # construct a dp matrix that row, col represents profit and group, entry is number of schemas
        dp = [[0] * (G+1) for _ in range(P+1)]
        dp[0][0] = 1
        for g0, p0 in zip(group, profit):
            # copy previous dp
            dp2 = [row[:] for row in dp]
            for p1 in range(P+1):
                # all schemas >= P will be put in Pth row
                p2 = min(P, p1 + p0)
                for g1 in range(G - g0 + 1):
                    g2 = g1 + g0
                    dp2[p2][g2] += dp[p1][g1]
                    dp2[p2][g2] %= mod
            dp = dp2
        
        return sum(dp[-1]) % mod

