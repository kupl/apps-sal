class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        res = 0
        for i, num in enumerate(A):
            if not stack or A[stack[-1]] > num:
                stack.append(i)
        for j in range(len(A) - 1, -1, -1):
            while stack and A[stack[-1]] <= A[j]:
                res = max(res, j - stack.pop())
        return res
