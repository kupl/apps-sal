class Solution:
    base = 'abc'
    base_len = 3

    def isValid(self, S: str) -> bool:
        stack = []
        for c in S:
            stack.append(c)
            if len(stack) >= 3:
                if stack[-1] == 'c' and stack[-2] == 'b' and (stack[-3] == 'a'):
                    stack.pop()
                    stack.pop()
                    stack.pop()
        return len(stack) == 0
