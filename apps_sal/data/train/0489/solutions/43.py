class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        res = 0
        for i, a in enumerate(A):
            if stack and A[stack[-1]] <= a:
                j = len(stack) - 1

                while j >= 0 and A[stack[j]] <= a:
                    res = max(res, i - stack[j])
                    j -= 1
            else:
                stack.append(i)

        return res
