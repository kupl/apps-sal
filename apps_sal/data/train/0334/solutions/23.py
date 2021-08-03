class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0
        array = list(s)
        i = 0
        while i <= len(array) - 2:
            if array[i] == array[i + 1]:
                res += min(cost[i], cost[i + 1])
                cost[i + 1] = max(cost[i], cost[i + 1])
            i += 1
        return res
