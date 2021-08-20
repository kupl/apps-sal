class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        (stack, ret) = ([], 0)
        for (i, a) in enumerate(A):
            if not stack or A[stack[-1]] > a:
                stack.append(i)
        for i in reversed(range(len(A))):
            while stack and A[stack[-1]] <= A[i]:
                ret = max(ret, i - stack.pop())
        return ret
