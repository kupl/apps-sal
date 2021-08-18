class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c not in [',', ')']:
                stack.append(True if c == 't' else False if c == 'f' else c)
            elif c == ')':
                seen = set()
                while stack[-1] != '(':
                    seen.add(stack.pop())
                stack.pop()
                operator = stack.pop()
                stack.append(all(seen) if operator == '&' else any(seen) if operator == '|' else not seen.pop())

        return stack[-1]
