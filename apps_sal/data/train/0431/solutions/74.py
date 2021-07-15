class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        res = 0
        A = [0] + A + [0]
        stack = []
        for i in range(len(A)):
            while stack and A[stack[-1]] > A[i]:
                j = stack.pop()
                res += A[j] * (i-j) * (j-stack[-1])
            stack.append(i)
        return res % (10**9+7)
