from collections import defaultdict

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestArithSeqLength(self, A: List[int]) -> int:
        sol = defaultdict(int)
        
        n = len(A)
        for i in range(n):
            for j in range(i):
                d = A[i] - A[j]
                sol[(i, d)] = max(sol[(i, d)], 1 + sol[(j, d)])
                
        return max(list(sol.values()), default=0) + 1
    
#         rows = len(A)
#         cols = len(A)
#         dp = [[2 for c in range(cols)] for r in range(rows)]
        
#         for c in range(cols): 
#             for r in range(0, c):
                
                
#         for c in range(cols): 
#             for r in range(0, c):
#                 diff = A[c] - A[r]             
#                 x = A[r] - diff 
#                 # search for k such that dp[k][r] A[k]=x
#                 for k in reversed(range(0, r)): # put this in doc
#                     if(A[k] == x):
#                         dp[r][c] = max(dp[k][r] + 1, dp[r][c])
#                         break
#         max_so_far = dp[0][0]
        
#         for c in range(cols): 
#             for r in range(0, c):
#                 max_so_far = max(max_so_far, dp[r][c])
        
#         return max_so_far
                
                

