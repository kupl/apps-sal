class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        left = True
        determined = False
        for i, c in enumerate(s1):
            if c > s2[i]:
                if not left and determined:
                    return False
                determined = True
            elif c < s2[i]:
                if left and determined:
                    return False
                left = False
                determined = True
        return True
