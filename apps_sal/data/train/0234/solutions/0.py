class Solution:

    def minAddToMakeValid(self, S: str) -> int:
        if not S:
            return 0
        stack = []
        add = 0
        for c in S:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    add += 1
        add += len(stack)
        return add
