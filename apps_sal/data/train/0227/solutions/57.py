class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        
        i = 0
        res = 0
        for j, a in enumerate(A):            
            if a == 0:
                K-=1                   
            while K < 0:
                if A[i] == 0:
                    K+=1
                i+=1                
            else:
                res = max(res, j-i+1)
        return res
