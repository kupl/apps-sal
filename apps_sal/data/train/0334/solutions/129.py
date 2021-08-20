class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        (head_idx, tail_idx) = (0, 1)
        total_cost = 0
        while tail_idx < len(s):
            if s[head_idx] == s[tail_idx]:
                if cost[head_idx] < cost[tail_idx]:
                    total_cost += cost[head_idx]
                    (head_idx, tail_idx) = (tail_idx, tail_idx + 1)
                else:
                    total_cost += cost[tail_idx]
                    tail_idx += 1
            else:
                (head_idx, tail_idx) = (tail_idx, tail_idx + 1)
        return total_cost
