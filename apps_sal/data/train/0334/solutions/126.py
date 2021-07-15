class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        cumu_cost = 0
        max_cost = None
        
        prev_char = None
        prev_cost = None
        
        result = 0
        
        for char, v in zip(s, cost):
            
            if prev_char and prev_char == char:
                if max_cost is None:
                    cumu_cost += v + prev_cost
                    max_cost = max(v, prev_cost)
                else:
                    cumu_cost += v
                    max_cost = max(max_cost, max(v, prev_cost))
                
            elif prev_char and prev_char != char and max_cost is not None:
                
                result += cumu_cost - max_cost
                cumu_cost = 0
                max_cost = None
                
                
                
        
            prev_char = char
            prev_cost = v
        
        if prev_char and max_cost is not None:
            result += cumu_cost - max_cost
        
        return result

        


