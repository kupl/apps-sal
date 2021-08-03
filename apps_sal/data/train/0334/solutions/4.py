class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        s = list(s)
        ct = 0
        i = 0
        while i <= len(s) - 2:
            if s[i] == s[i + 1]:
                cos = min(cost[i], cost[i + 1])
                cmax = max(cost[i], cost[i + 1])
                ct += cos
                cost[i + 1] = cmax
                i += 1
            else:
                i += 1
        return ct
