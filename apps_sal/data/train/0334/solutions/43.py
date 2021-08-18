class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = prev = 0
        for i in range(1, len(s)):
            if s[prev] != s[i]:
                prev = i
            else:
                res += min(cost[prev], cost[i])
                if cost[prev] < cost[i]:
                    prev = i
        return res
