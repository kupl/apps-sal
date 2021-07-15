class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 3:
            i = s.find('abc')
            if i == -1:
                return False
            s = s[:i] + s[i + 3:]
        return not s or s == 'abc'
