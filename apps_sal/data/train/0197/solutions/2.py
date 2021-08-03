class Solution:
    def isValid(self, S: str) -> bool:
        l = ''
        for c in S:
            l += c
            if l[-3:] == 'abc':
                l = l[:-3]
        return not l
