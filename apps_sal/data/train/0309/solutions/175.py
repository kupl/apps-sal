class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
#         n = len(A);
#         res = 1;
        
#         for i in range(1,n):
#             for j in range(i):
#                 count = 2; 
#                 x = i + 1;
#                 y = i;
                
#                 while x < n and y < n:
#                     if A[x] - A[y] == A[i] - A[j]:
#                         count += 1;
#                         y = x
#                     x += 1;
#                 res = max(res, count);
        
#         return res;

        
        dp = dict();
        n = len(A);
        for i in range(n):
            for j in range(i+1,n):
                dp[(j, A[j] - A[i])] = dp.get((i, A[j] - A[i]), 1) + 1;
        
        return max(dp.values());
                
        
                        
                
                

