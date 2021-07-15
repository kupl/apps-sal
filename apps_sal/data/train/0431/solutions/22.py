class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        mod = 10**9+7
        A = [0] + A + [0]
        n = len(A)
        stack = []
        res = 0
        
        for i in range(n):
            while stack and A[stack[-1]]>A[i]:
                curr = stack.pop(-1)
                left = stack[-1]
                right = i
                res += A[curr]*(curr-left)*(right-curr)   
            stack.append(i)
        res %= 10 ** 9 + 7
        return res

