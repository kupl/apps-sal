class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def recur(index, prev_color, neighbor_count):
            if index == m:
                return 0 if neighbor_count == target else float('inf')
            if houses[index] != 0:
                return recur(index + 1, houses[index], neighbor_count + int(prev_color != houses[index]))
            total = float('inf')
            for color in range(1, n + 1):
                total = min(total, cost[index][color - 1] + recur(index + 1, color, neighbor_count + int(prev_color != color)))
            return total
        final_ans = recur(0, -1, 0)
        return final_ans if final_ans != float('inf') else -1
