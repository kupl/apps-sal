class Solution:
    def isValid(self, s: str) -> bool:
        while s:
            tmp = s.replace('abc', '')
            if tmp == s:
                break
            s = tmp
        return not s
