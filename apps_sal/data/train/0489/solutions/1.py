class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        n = len(A)
        for i in range(n):
            if not stack or A[stack[-1]] > A[i]:
                stack.append(i)

        res = 0
        i = n - 1
        while i > res:
            while stack and A[stack[-1]] <= A[i]:
                res = max(res, i - stack[-1])
                stack.pop()
            i -= 1
        return res
