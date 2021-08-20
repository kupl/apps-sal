class Solution:

    def isValid(self, S: str) -> bool:
        stack = []
        for c in S:
            stack.append(c)
            while stack and stack[-1] == 'c' and (len(stack) >= 3) and (stack[-2] == 'b') and (stack[-3] == 'a'):
                stack = stack[:-3]
        return not stack
