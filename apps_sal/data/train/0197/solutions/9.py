# class Solution:
#     def isValid(self, s: str) -> bool:
#         element = 0
#         lg = len(s)
#         for j in range(lg):
#             element += 1
#             if element >= 3:
#                 if s[2]=='c' and s[1]=='b' and s[0]=='a':
#                     for i in range(2,-1,-1):
#                         del s[i]

#         return len(s)==0
            
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stk = deque()
        for st in s:
            stk.append(st)
            if len(stk) >= 3:
                if stk[-1]=='c' and stk[-2]=='b' and stk[-3]=='a':
                        for i in range(3):
                            stk.pop()
        return len(stk)==0

