class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        N = len(A)
        stack = []
        res = 0
        for (i, a) in enumerate(A):
            if not stack or stack[-1][1] > a:
                stack.append((i, a))
            else:
                x = len(stack) - 1
                while x >= 0 and stack[x][1] <= a:
                    res = max(res, i - stack[x][0])
                    x -= 1
        return res
