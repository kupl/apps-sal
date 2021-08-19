class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        total_cost = 0
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                j = i + 1
                while j < len(s) and s[j] == s[i]:
                    j += 1
                total_cost += sum(cost[i:j]) - max(cost[i:j])
                i = j
            else:
                i += 1
        return total_cost
