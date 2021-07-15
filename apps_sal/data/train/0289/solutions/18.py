from functools import reduce

class Solution:
        
    
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        
        lsum = []
               
        csum = reduce(lambda a,b:a+b, A[:L]) 
        lsum.append(csum)
        
        for i in range(L, len(A)):
            csum += A[i] - A[i-L]
            lsum.append(csum)
            
        msum = []
        csum = reduce(lambda a,b:a+b, A[:M])
            
        msum.append(csum)
        
        for i in range(M, len(A)):
            csum += A[i] - A[i-M]
            msum.append(csum)
            
        maxSum = 0
        for i in range(len(A)-L+1):
            ls = i
            le = i + L - 1
            
            for j in range(len(A) - M+1):
                ms = j
                me = j + M - 1
                
                if (le < ms) or (me < ls):
                    maxSum = max(maxSum, lsum[ls] + msum[ms])
                    
        return maxSum    
