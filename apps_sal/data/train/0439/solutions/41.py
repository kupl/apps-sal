class Solution:
    
    def maxTurbulenceSize(self, A: List[int]) -> int:
        def sign(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0
        
        if len(A) == 1:
            return 1
        
        if len(A) == 2:
            if A[0] != A[1]:
                return 2
            else:
                return 1
        
        
        prev = int(A[0] != A[1]) + 1
        ans = prev
        
        for i in range(2, len(A)):
            curr_sign = sign(A[i]-A[i-1])
            prev_sign = sign(A[i-1]-A[i-2])
            
            if curr_sign == 0:
                prev = 1
            elif curr_sign != prev_sign:
                prev = prev + 1
            else:
                prev = 2
            
            ans = max(ans, prev)
        return ans
