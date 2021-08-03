class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        fee = max_cost = 0
        for i, cst in enumerate(cost):
            if i > 0 and s[i] != s[i - 1]:
                max_cost = 0
            fee += min(cst, max_cost)
            max_cost = max(cst, max_cost)
        return fee
