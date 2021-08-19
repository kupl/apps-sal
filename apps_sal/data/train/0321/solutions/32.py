class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1sorted = ''.join(sorted(s1))
        s2sorted = ''.join(sorted(s2))
        res1 = True
        res2 = True
        for i in range(len(s1)):
            if ord(s1sorted[i]) > ord(s2sorted[i]):
                res1 = False
        for i in range(len(s1)):
            if ord(s1sorted[i]) < ord(s2sorted[i]):
                res2 = False
        return res1 or res2
