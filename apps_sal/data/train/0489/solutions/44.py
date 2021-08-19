class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        res = 0
        stack = []
        for (i, a) in enumerate(A):
            if not stack or stack[-1][1] > a:
                stack.append((i, a))
            else:
                N = len(stack) - 1
                while N >= 0 and stack[N][1] <= a:
                    res = max(res, i - stack[N][0])
                    N = N - 1
        return res
