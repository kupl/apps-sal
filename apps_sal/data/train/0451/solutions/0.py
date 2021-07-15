import math
class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        if len(S) == 0 or len(T) == 0:
            return False
        def process(s):
            if s[-1] == '.':
                s = s[:-1]
            stack, repeat_9 = [], False
            for i, x in enumerate(s):
                if x != ')':
                    stack.append(x)
                else:
                    tmp = ''
                    while stack[-1] != '(':
                        tmp += stack.pop()
                    if len(tmp) == tmp.count('9'):
                        repeat_9 = True
                    stack.pop()
                    return ''.join(stack) + tmp[::-1] * (24 // len(tmp)), repeat_9
            return ''.join(stack), repeat_9
        
        x, y = process(S), process(T)
        if x[0].count('.') == 0 or y[0].count('.') == 0:
            return float(x[0]) == float(y[0])
        l = max(len(x[0]), len(y[0]))
        if x[0][:17] == y[0][:17]:
            return True
        if x[1] or y[1]:
            m = min(len(x[0].split('.')[1]), len(y[0].split('.')[1]))
            if round(float(x[0]), m) == round(float(y[0]), m):
                return True
        
        return False
        

