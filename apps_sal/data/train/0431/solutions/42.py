class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = pow(10,9)+7
        N = len(A)
        prev = [None]*N
        next_ = [None]*N
        
        stack=[]
        for i in range(N):
            while stack and A[i]<=A[stack[-1]]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack=[]
        for k in range(N-1,-1,-1):
            while stack and A[k]<A[stack[-1]]:
                stack.pop()
            next_[k] = stack[-1] if stack else N
            stack.append(k)
        
        # print(prev)
        # print(next_)
        
        return sum((i-prev[i])*(next_[i]-i)*A[i] for i in range(N))%MOD

