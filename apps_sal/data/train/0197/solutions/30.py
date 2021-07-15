class Solution:
    def isValid(self, s: str) -> bool:
        while s.find('abc') > -1:
            i = s.find('abc')
            s = s[:i] + s[i+3:]
        return s == ''
        

