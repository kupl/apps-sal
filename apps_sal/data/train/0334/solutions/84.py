class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0

        if len(s) <= 1:
            return 0

        i = 0
        while i < len(s) - 1:
            j = i
            costs = []
            isCost = False
            while j <= len(s) - 2 and s[j + 1] == s[i]:
                isCost = True
                costs.append(cost[j])
                j += 1
            if isCost:
                costs.append(cost[j])
            res += sum(sorted(costs, reverse=True)[1:])
            i = j
            i += 1

        return res
