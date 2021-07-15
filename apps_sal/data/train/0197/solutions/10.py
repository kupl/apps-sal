class Solution:
    def isValid(self, s: str) -> bool:
        LAST_THREE = ['a','b','c']
        stack = [] 
        
        for index, _chr in enumerate(s):
            stack.append(_chr)
            if stack[-3:] == LAST_THREE:
                stack.pop()
                stack.pop()
                stack.pop()
                
        return len(stack) == 0
