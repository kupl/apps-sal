class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) < 2:
            return 0
        f = 0
        i = 0
        s = list(s)
        while i < len(s) - 1:
            v1 = s[i]
            v2 = s[i + 1]
            if v1 == v2:
                c1 = cost[i]
                c2 = cost[i + 1]
                if c1 < c2:
                    f += c1
                else:
                    f += c2
                    cost[i + 1] = c1
            i += 1
        return f
