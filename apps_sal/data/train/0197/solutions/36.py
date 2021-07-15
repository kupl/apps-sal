'''
abc abc
a abc bc
ab abc c

Keep a stack that remembers the current letter for each depth level

for example:
aabcbc
  123
1 [a, b]
2 [a]
3 [b]

'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        
        for ch in s:
            if ch == 'a':
                stack.append('a')
            elif ch == 'b':
                if stack and stack[-1] == 'a':
                    stack[-1] = 'b'
                else:
                    return False
            elif ch == 'c':
                if stack and stack[-1] == 'b':
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return (len(stack) == 0)
