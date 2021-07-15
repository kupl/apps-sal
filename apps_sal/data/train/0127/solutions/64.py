from collections import defaultdict

class Solution:
    MOD = 10**9 + 7
    
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        remaining_profit = sum(profit)
        
        schemes, next_schemes = defaultdict(int), defaultdict(int)
        schemes[(0, 0)] = 1
        for i, p in enumerate(profit):
            remaining_profit -= p
            
            for curr_g, curr_p in [(0, 0), (group[i], profit[i])]:
                for prev_g, prev_p in schemes:
                    next_g = prev_g + curr_g
                    next_p = min(prev_p + curr_p, P)

                    if next_p + remaining_profit >= P and next_g <= G:
                        next_schemes[(next_g, next_p)] += schemes[(prev_g, prev_p)]
                    
            schemes, next_schemes = next_schemes, defaultdict(int)
            for k in schemes:
                schemes[k] = schemes[k] % Solution.MOD
            
        return sum(schemes.values()) % Solution.MOD
