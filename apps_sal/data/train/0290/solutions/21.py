class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        visited = {}  # map (start, end) -> min cost
        
        def minCostHelper(start, end):            
            # check if cached
            if (start, end) in visited:
                return visited[(start, end)]
            
            # if not, calculate
            min_cost = float('inf')
            for c in cuts:
                if c <= start or c >= end:
                    continue
                cost = (end-start) + minCostHelper(start, c) + minCostHelper(c, end)
                min_cost = min(min_cost, cost)
                
            if min_cost == float('inf'):
                min_cost = 0
                
            visited[(start, end)] = min_cost
            return min_cost
        
        return minCostHelper(0, n)

