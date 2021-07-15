class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7           
        n = len(A)
        
        # previous less element
        stack = []
        left = [None] * n
        for i in range(n):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)
        # next less element
        # stack = []
        # right = [None] * n
        # for i in range(n-1,-1,-1):
        #     # note A[i] < A[stack[-1]]
        #     while stack and A[i] < A[stack[-1]]:
        #         stack.pop()
        #     # note right[i] = n if not stack
        #     right[i] = stack[-1] if stack else n
        #     stack.append(i)
        stack = []
        right = [n] * n
        for i in range(n):
            while stack and A[i] <= A[stack[-1]]:
                right[stack.pop()] = i
            stack.append(i)
        
        res = 0
        for i in range(n):
            res += (i-left[i]) * (right[i]-i) * A[i]
        
        return res % MOD
