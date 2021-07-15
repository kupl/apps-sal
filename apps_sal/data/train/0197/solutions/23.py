class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            ns = s.replace('abc', '')
            if ns == '':
                return True
            if ns == s:
                return False
            s = ns
