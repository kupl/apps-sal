class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        BOUND = (10 ** 9) + 7
        dp = {}
        
        def f(g, p, i):
            if (g, p, i) in dp:
                return dp[(g, p, i)]
            
            if g == 0:
                return 0
            if i == 0:
                return 1 if group[0] <= g and profit[0] >= p else 0
            
            res = f(g, p, i-1)
            
            if group[i] <= g:
                if profit[i] >= p:
                    res += 1
                res += f(g-group[i], max(0,p-profit[i]), i-1)
                
            dp[(g,p,i)] = res % BOUND
            return dp[(g,p,i)]
        
        return f(G, P, len(group) - 1)
