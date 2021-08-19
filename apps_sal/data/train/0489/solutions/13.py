class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        for (i, v) in enumerate(A):
            if i == 0 or v < A[stack[-1]]:
                stack.append(i)
        ans = 0
        for i in range(len(A) - 1, -1, -1):
            while stack and A[i] >= A[stack[-1]]:
                ans = max(ans, i - stack.pop())
        return ans
