class Solution:
    def isValid(self, s: str) -> bool:
        
        
        stack = []
        
        for c in s:
            if c == 'c':
                if ''.join(stack[-2:]) == 'ab':
                    stack.pop()
                    stack.pop()
                    continue
            stack.append(c)
        
        return not stack
