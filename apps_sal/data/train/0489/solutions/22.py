class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # decreasing stack
        stack = []
        for i, a in enumerate(A):
            if not stack or a < A[stack[-1]]:
                stack.append(i)
        ans = 0
        for i in range(len(A) - 1, -1, -1):
            while stack and A[stack[-1]] <= A[i]:
                ans = max(ans, i - stack[-1])
                stack.pop()
        return ans
