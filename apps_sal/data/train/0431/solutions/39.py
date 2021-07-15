class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        res = 0
        #stack store the index of non-decreasing numbers
        stack = []
        A = [float('-inf')] + A + [float('-inf')]
        
        for i, n in enumerate(A):
            #if n is smaller than the last element in stack
            #pop until it is the largest
            while stack and A[stack[-1]] > n:
                cur = stack.pop()
                #after pop, the stack[-1] has the index of the first element that is smaller than cur. i is the right boundary 
                res += A[cur] * (cur - stack[-1]) * (i - cur)
            stack.append(i)
        
        return res % (10**9+7)
