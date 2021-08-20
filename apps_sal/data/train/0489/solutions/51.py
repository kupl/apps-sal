class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        (stack, ans) = ([], 0)
        for (i, val) in enumerate(A):
            if not stack or A[stack[-1]] > val:
                stack.append(i)
        for j in reversed(list(range(len(A)))):
            while stack and A[stack[-1]] <= A[j]:
                ans = max(ans, j - stack.pop())
        return ans
