class Solution:
    def isValid(self, s: str) -> bool:
        while s:
            if 'abc' not in s:
                return False
            j = 0
            while j < len(s) - 2:
                if s[j:j+3] == 'abc':
                    s = s[:j] + s[j+3:]
                else:
                    j += 1
        return True
