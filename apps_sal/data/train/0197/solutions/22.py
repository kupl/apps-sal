class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        i=0
        while(i<len(s) or (stack and len(stack)>2 and stack[-3:]==['a','b','c'])):
            while(stack and len(stack)>2 and stack[-3:]==['a','b','c']):
                
                stack.pop()
                stack.pop()
                stack.pop()
            if i<len(s):
                stack.append(s[i])
                i+=1
        #print('stack',stack)
        if not stack:
            return True
        return False
