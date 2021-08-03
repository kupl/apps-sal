class Solution:
    def isValid(self, S: str) -> bool:
        i = S.find('abc')
        while i != -1:
            S = S[:i] + S[i + 3:]
            i = S.find('abc')
        return not S
