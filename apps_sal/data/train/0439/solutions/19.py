class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n=len(A)
        window_start = 0
        max_len = 1 
        
        def cmp(a, b): 
            if a<b: 
                return -1
            elif a>b: 
                return 1
            return 0 
        
        for window_end in range(1, n): 
            c= -1 if A[window_end-1] < A[window_end] else 1
            
            if A[window_end-1]-A[window_end]==0: 
                window_start = window_end
            elif window_end==n-1 or c*cmp(A[window_end], A[window_end+1])!=-1: 
                max_len = max(max_len, window_end - window_start + 1)
                window_start = window_end
                
        return max_len
            
            

