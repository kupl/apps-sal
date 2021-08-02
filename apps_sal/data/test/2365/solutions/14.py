class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for ch in expression:
            if ch == ',':
                continue
            if ch != ')':
                stack.append(ch)
            else:
                temp = ''
                while stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                if stack[-1] == '&':
                    res = 't' if temp.count('f') == 0 else 'f'
                elif stack[-1] == '|':
                    res = 'f' if temp.count('t') == 0 else 't'
                else:
                    res = 't' if temp == 'f' else 'f'
                stack[-1] = res
        return True if stack[-1] == 't' else False
