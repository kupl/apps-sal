class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:

        s = [0]

        for x in A:
            s += s[-1] + x,

        stack = []
        res = len(s) + 1

        for i, x in enumerate(s):

            while stack and x <= s[stack[-1]]:
                stack.pop()

            while stack and x - s[stack[0]] >= K:
                res = min(res, i - stack.pop(0))

            stack += i,

        return res if res < len(s) + 1 else -1
