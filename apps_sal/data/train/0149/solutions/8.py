class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        while True:
            stk = []
            s_new = []
            for c in s:
                if len(stk) == k:
                    stk = []
                while stk and c != stk[-1]:
                    s_new.append(stk.pop())
                stk.append(c)
                if len(stk) == k:
                    stk = []
            while stk:
                s_new.append(stk.pop())
            print(''.join(s_new))
            if s == s_new:
                break
            s = s_new
        return ''.join(s)
