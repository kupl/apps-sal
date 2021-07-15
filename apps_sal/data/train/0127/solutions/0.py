class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        group_len, profit_len = len(group),len(profit)
        dp = [[0]*(G+1) for _ in range(P+1)]
        dp[0][0] = 1
        for pro, gro in zip(profit,group):
            dp2 = [x[:] for x in dp]
            for p1 in range(P+1):
                p = min(pro + p1,P)
                for g1 in range(G+1-gro):
                    g = g1 + gro
                    dp2[p][g] += dp[p1][g1]
                    dp2[p][g] %= MOD
            dp = dp2
        return sum(dp[-1]) %MOD
