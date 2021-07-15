class Node:
    def __init__(self, idx, l, r):
        self.idx = idx
        self.l = l
        self.r = r
        self.left_node = self
        self.right_node = self
        

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
    
        solved = dict()
    
        def cost(l, r):
            if l == r: return 0
            if (l, r) in solved:
                return solved[(l, r)]
            
            min_cost = float('inf')
            for c in cuts:
                if c > l and c < r:
                    min_cost = min(min_cost, r - l + cost(l, c) + cost(c, r))
            
            if min_cost == float('inf'): return 0
            
            solved[(l, r)] = min_cost
            return min_cost
        
        return cost(0, n)
        
        
'''

cost(0, l - 1) -> min(cost(0, r) + cost(r, l - 1)) for r in cuts


'''
        

