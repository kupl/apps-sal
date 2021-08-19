class Solution:
    def profitableSchemes(self, G, P, group, profit):
        dp = [[0] * (G + 1) for i in range(P + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    dp[min(i + p, P)][j + g] += dp[i][j]
        return sum(dp[P]) % (10**9 + 7)
    # def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
    #     schemes=[(pro, kitnelog) for pro, kitnelog in zip(profit, group)]
    #     nonlocal dump
    #     dump={}
    #     nonlocal dump1
    #     dump1={}
    #     return self.getans(G, P, schemes)
    # def getans(self, g, p, schemes, mod=(10**9+7)):
    #     nonlocal dump
    #     nonlocal dump1
    #     if len(schemes)==0:
    #         if p<=0:
    #             return 1
    #         return 0
    #     if g<=0 and p>0:
    #         return 0
    #     if p<=0:
    #         return self.numsubsetslessthan(g, schemes)
    #     if (g, p, len(schemes)) in dump:
    #         return dump[(g, p, len(schemes))]
    #     a=self.getans(g-schemes[-1][1], p-schemes[-1][0], schemes[:-1]) if g>=schemes[-1][1] else 0
    #     b=self.getans(g, p, schemes[:-1])
    #     dump[(g, p, len(schemes))]=(a+b)%mod
    #     return dump[(g, p, len(schemes))]
    # def numsubsetslessthan(self, g, schemes, mod=10**9+7):
    #     nonlocal dump1
    #     if len(schemes)==0:
    #         return 1
    #     if (g, len(schemes)) in dump1:
    #         return dump1[(g, len(schemes))]
    #     a=self.numsubsetslessthan(g-schemes[-1][1], schemes[:-1]) if g>=schemes[-1][1] else 0
    #     b=self.numsubsetslessthan(g, schemes[:-1])
    #     dump1[(g, len(schemes))]=(a+b)%mod
    #     return dump1[(g, len(schemes))]
