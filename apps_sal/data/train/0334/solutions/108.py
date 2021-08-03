class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0
        i = 1
        temp = cost[0]
        while i < len(cost):
            if s[i - 1] == s[i]:
                res += min(temp, cost[i])
                temp = max(temp, cost[i])
            else:
                temp = cost[i]
            i += 1
        return res
