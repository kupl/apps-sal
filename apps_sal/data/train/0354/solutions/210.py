class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        memo ={}
        
        def dfs(nLeft, last, curLen):
            if (nLeft, last, curLen) in memo:
                return memo[(nLeft, last, curLen)]
            if nLeft == 0:
                return 1
            cnt = 0
            for i in range(6):
                if i==last and rollMax[i] == curLen:
                    continue
                cnt += dfs(nLeft-1, i, curLen+1 if i==last else 1 )
            
            memo[(nLeft, last, curLen)] = cnt
            return memo[(nLeft, last, curLen)]
                    
        return dfs(n, 0, 0)%(10**9+7)
    
    
#         self.res = 0
        
        
#         def dfs(nLeft, last, curLen):
#             if nLeft == 0:
#                 self.res += 1
#                 return
            
#             for i in range(6):
#                 if i==last and rollMax[i] == curLen:
#                     continue
#                 dfs(nLeft-1, i, curLen+1 if i==last else 1 )
#             return
            
#         dfs(n, 0, 0)
        
#         return self.res
    

