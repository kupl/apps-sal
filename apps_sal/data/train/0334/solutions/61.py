class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        _min = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                _min += min(cost[i], cost[i + 1])
                if cost[i] >= cost[i + 1]:
                    cost[i + 1] = cost[i]
        return _min
