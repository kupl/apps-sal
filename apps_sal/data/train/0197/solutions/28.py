class Solution:

    def isValid(self, S: str) -> bool:
        stack = []
        for c in S:
            stack.append(c)
            if ''.join(stack[-3:]) == 'abc':
                stack = stack[:-3]
        return len(stack) == 0
