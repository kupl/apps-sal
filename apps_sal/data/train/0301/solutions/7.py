class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        return self.findMaxConnectLines(0, 0, A, B, {})
        
        
    def findMaxConnectLines(self, i, j, A, B, dic):
        if i == len(A) or j == len(B):
            return 0
        
        if (i, j) in dic: return dic[(i, j)]
        
        a = self.findMaxConnectLines(i+1, j, A, B, dic)
        b = float('-inf')
        for k in range(j, len(B)):
            if B[k] == A[i]:
                b = self.findMaxConnectLines(i+1, k+1, A, B, dic) + 1
                break
        dic[(i, j)] = max(a, b)
        return dic[(i, j)]
        
        
        
#   1, 4, 2 ,3, 5
#   1, 2, 3, 5, 4
#   every number has choices: not connect or connect (first encounter connect)
# 

