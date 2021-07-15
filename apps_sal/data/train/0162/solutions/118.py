class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def helper(i, j):
            if (i,j) in self.h:
                return self.h[i,j]
            
            if i == n1 or j==n2:
                self.h[i,j] = 0
                return 0

            if text1[i]==text2[j]:
                self.h[i,j] = helper(i+1, j+1)+1
            else:
                self.h[i,j] = max(helper(i+1, j), helper(i, j+1))
            
            return self.h[i,j]
                
        
        n1 = len(text1)
        n2 = len(text2)
        
        self.h = {}
        
        res = helper(0, 0)
        
        return res
        
#         n1 = len(text1)
#         n2 = len(text2)
#         s1 = '*'+text1
#         s2 = '*'+text2
        
#         if n1==0 or n2==0:
#             return 0
        
#         res = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        
#         for i in range(1, n1+1):
#             for j in range(1, n2+1):
#                 if s1[i] == s2[j]:
#                     res[i][j] = res[i-1][j-1]+1
#                 else:
#                     res[i][j] = max(res[i][j-1], res[i-1][j])
        
#         return res[-1][-1]

