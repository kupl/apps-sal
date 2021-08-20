class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            stack.append(c)
            while ''.join(stack[-3:]) == 'abc':
                stack = stack[:-3]
        if stack:
            return False
        else:
            return True
