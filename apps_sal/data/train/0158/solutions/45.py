from functools import lru_cache
class Solution:
    @lru_cache(None)
    def kSimilarity(self, A: str, B: str) -> int:
        if len(A)==0:
            return 0
        
        if A[0]==B[0]:
            return self.kSimilarity(A[1:],B[1:])
        
        for i in range(1,len(B)):
            if A[0]==B[i] and B[0]==A[i]:
                return 1 + self.kSimilarity(A[1:i]+A[i+1:], B[1:i]+B[i+1:])
            
        ans = math.inf
        for i in range(1,len(B)):
            if A[0]==B[i]: ans = min(ans, 1+self.kSimilarity(A[1:], B[1:i]+B[0]+B[i+1:]))
        
        return ans
