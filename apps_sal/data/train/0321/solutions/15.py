class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ss1 = sorted(s1)
        ss2 = sorted(s2)
        f = True
        r = True
        for (x, y) in zip(ss1, ss2):
            f = f and x >= y
            r = r and x <= y
        return f or r
