class Solution:

    def check(self, d1, d2):
        for (x, y) in zip(d1, d2):
            if x <= y:
                continue
            return False
        return True

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        d1 = sorted(s1)
        d2 = sorted(s2)
        return self.check(d1, d2) | self.check(d2, d1)
