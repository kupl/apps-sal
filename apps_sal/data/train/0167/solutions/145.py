import numpy as np
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # given K eggs and M moves, what is the maximum number of floor that we can check.
        dp = [[0 for i in range(K+1)] for j in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, K+1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + 1
            if dp[i][j] >= N:
                return i
                
                
                
#         #Dec1, 2019
#         self.grid = np.zeros((K+1, N+1), dtype=np.int32)
#         return self.drop(K, N)
        
#     def drop(self, K, N):
#         for j in range(1, N+1):
#             for i in range(1, K+1):
#                 self.grid[i][j] = self.grid[i-1][j-1] + self.grid[i][j-1] + 1
#             if self.grid[K][j] >= N: #if we could already check all stairs with K eggs, then return the number of stairs j
#                 return j
#         return self.grid[K][N]
        

#         #Dec1, 2019
#         self.grid = np.zeros((K+1, N+1), dtype=np.int32)
#         return self.test(K, N)
        
        
#     def test(self, K, N):
#         if N == 1 or N == 0:
#             return N
#         elif K == 1 or K == 0:
#             return N
#         else:
#             if self.grid[K][N]:
#                 return self.grid[K][N]
#             else:
#                 self.grid[K][N] = min(max(self.test(K-1, i-1), self.test(K, N-i)) for i in range(1, N+1))+1
#                 return self.grid[K][N]

