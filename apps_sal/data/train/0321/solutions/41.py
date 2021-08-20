class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)

        def check(s1, s2):
            c = 0
            n = len(s1)
            for i in range(n):
                if s1[i] >= s2[i]:
                    c = c + 1
            return c == n
        return check(s2, s1) or check(s1, s2)
