class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        
        
        dp = [[0] * (G+1) for i in range(P+1)]
        dp[0][0] = 1
        n = len(group)
        for k in range(n):
            g, p = group[k], profit[k]
            for i in range(P, -1, -1):
                for j in range(G-g, -1, -1):
                    dp[min(i+p, P)][j+g] += dp[i][j]
        return sum(dp[P]) % (10 ** 9 + 7)
            
            
         
#         n = len(group)
#         dp = {\"\":(0, 0)}
#         count = 0
#         for i in range(n):
#             g, p = group[i], profit[i]
#             if g <= G:
#                 for k, v in list(dp.items()):
#                     pg, pp = v
#                     if pg + g <= G:
#                         if pp + p >= P:
#                             count += 1
#                         dp[k+str(i)] = (pg+g, pp+p)
#         return count % (10**9+7)
            
            
        
        

