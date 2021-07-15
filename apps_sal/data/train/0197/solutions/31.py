class Solution:
    def isValid(self, s: str) -> bool:
        while s.find('abc') >= 0:
            s = s.replace('abc', '')
        return s == ''
