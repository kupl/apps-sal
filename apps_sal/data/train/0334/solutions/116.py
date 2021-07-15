class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        prev_idx = None
        count = 0
        for ii in range(1, len(s)):
            b = s[ii]
            if prev_idx is None:
                prev_idx = ii - 1
            a = s[prev_idx]
            if a == b:
                cost_a = cost[prev_idx]
                cost_b = cost[ii]
                count += min(cost_a, cost_b)
                prev_idx = max([cost_a, prev_idx], [cost_b, ii])[1]
            else:
                prev_idx = None
        return count
