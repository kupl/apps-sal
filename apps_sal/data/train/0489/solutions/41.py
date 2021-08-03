class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)

        stack = []
        for i, num in enumerate(A):
            if not stack or num < A[stack[-1]]:
                stack.append(i)

        ans = 0
        for j in range(n - 1, -1, -1):
            while stack and A[j] >= A[stack[-1]]:
                ans = max(ans, j - stack.pop())
        return ans
