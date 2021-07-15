from functools import lru_cache

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        # K <= A <= 100
        # O((AK)^2) could work
        # Looks like dp
        
        @lru_cache(None)
        def rec(j,K):
            nonlocal A
            
            if K == 1:
                return sum(A[0:j+1])/(j+1)
            
            res = 0
            runningsum = 0
            for i in range(j, K-2, -1):
                runningsum += A[i]
                res = max(res, runningsum/(j - i + 1) + rec(i-1,K-1))
            return res
        
        return rec(len(A)-1, K)
            
        
        

