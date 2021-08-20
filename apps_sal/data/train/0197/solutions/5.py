class Solution:

    def isValid(self, s: str) -> bool:
        if len(s) % 3 != 0:
            return False
        if len(s) == 0:
            return True
        stack = []
        for i in s:
            if i != 'c':
                stack.append(i)
            elif len(stack) >= 2 and stack[-1] == 'b' and (stack[-2] == 'a'):
                stack.pop()
                stack.pop()
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        return False
