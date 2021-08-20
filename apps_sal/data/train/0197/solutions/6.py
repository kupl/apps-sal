class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == 'c':
                if len(stack) > 1 and stack[-1] == 'b' and (stack[-2] == 'a'):
                    stack.pop()
                    stack.pop()
            else:
                stack.append(ch)
        return not stack
