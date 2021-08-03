class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        f = 0
        while s:
            i = 0
            f = 0
            while i < l:
                if s[i] == 'a' and i + 1 < l and s[i + 1] == 'b' and i + 2 < l and s[i + 2] == 'c':
                    s = s[:i] + s[i + 3:]
                    l -= 3
                    f = 1
                else:
                    i += 1
            if f == 0 and l != 0 and s != '':
                return False
        return True
