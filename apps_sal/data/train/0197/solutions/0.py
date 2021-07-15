class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        return self.isValid(s.replace('abc', '')) if s.replace('abc', '') != s else False

