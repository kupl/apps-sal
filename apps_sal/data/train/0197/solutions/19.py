class Solution:
    def isValid(self, s: str) -> bool:
        findVal = s.find('abc')
        while findVal != -1:
            s = s[:findVal] + s[findVal + 3:]
            findVal = s.find('abc')
        return s == ''
