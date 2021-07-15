class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        for char in s:
            if char == 'c' and len(stack) >= 2:
                if stack[-1] == 'b' and stack[-2] == 'a':
                    stack.pop()
                    stack.pop()
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        return False
