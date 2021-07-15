class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        N = len(A)
        if N == 0: return 0
        mod = 10**9 + 7                
        
        stackLeft, stackRight, left, right = [], [], [0] * N, [0] * N
        
        for L in range(N):
            while stackLeft and A[stackLeft[-1]] > A[L]: stackLeft.pop()
            left[L] = L - (stackLeft[-1] if stackLeft else -1)       
            stackLeft.append(L)
            R = N - L - 1
            while stackRight and A[stackRight[-1]] >= A[R]: stackRight.pop()
            right[R] = stackRight[-1] - R if stackRight else N - R        
            stackRight.append(R)
            
        return sum([l*r*v for l,r,v in zip(left, right, A)]) % mod

