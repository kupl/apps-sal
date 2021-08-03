class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        prv = 0

        res = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if i - prv > 1:
                    mc = cost[prv]
                    for j in range(prv, i):
                        res += cost[j]
                        if cost[j] > mc:
                            mc = cost[j]
                    res -= mc
                prv = i

        if len(s) - prv > 1:
            mc = cost[prv]
            for j in range(prv, len(s)):
                res += cost[j]
                if cost[j] > mc:
                    mc = cost[j]
            res -= mc

        return res
