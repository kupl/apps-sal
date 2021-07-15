class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        return self.at_most(A, K) - self.at_most(A, K - 1)
    
    
    def at_most(self, A, K):
        if K == 0:
            return 0
        
        window = {}
        left = 0
        ret = 0
        
        for right in range(len(A)):
            window[A[right]] = window.get(A[right], 0) + 1
            
            while left < right and len(window) > K:
                window[A[left]] -= 1
                
                if window[A[left]] == 0:
                    del window[A[left]]
                
                left += 1
            
            ret += (right - left + 1)
        
        return ret
            

