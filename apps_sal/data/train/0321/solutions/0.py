from collections import Counter


class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        (d1, d2) = (Counter(s1), Counter(s2))
        return self.check(d1, d2) or self.check(d2, d1)

    def check(self, d1: dict, d2: dict) -> bool:
        s = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            s += d1[c] - d2[c]
            if s < 0:
                return False
        return True
