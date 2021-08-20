class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        stack = []
        for i in range(n):
            if not stack or A[stack[-1]] >= A[i]:
                stack.append(i)
        res = 0
        for i in range(n - 1, -1, -1):
            while stack and A[stack[-1]] <= A[i]:
                res = max(res, i - stack.pop())
        return res
