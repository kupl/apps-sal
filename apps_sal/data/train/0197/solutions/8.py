from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stk = deque()
        for st in s:
            stk.append(st)
            if len(stk) >= 3:
                if stk[-1] == 'c' and stk[-2] == 'b' and stk[-3] == 'a':
                    for i in range(3):
                        stk.pop()
        return len(stk) == 0
