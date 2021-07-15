class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        N = len(A)
        if N == 0: return 0
        mod = 10**9 + 7                
        
        stack, left, right = [], [0] * N, [0] * N
        
        for i in range(N):
            while stack and A[stack[-1]] > A[i]: stack.pop()
            left[i] = i - (stack[-1] if stack else -1)       
            stack.append(i)
            
        stack.clear() 
        
        for i in range(N - 1, -1, -1):
            while stack and A[stack[-1]] >= A[i]: stack.pop()
            right[i] = stack[-1] - i if stack else N - i        
            stack.append(i)
            
        return sum([l*r*v for l,r,v in zip(left, right, A)]) % mod

