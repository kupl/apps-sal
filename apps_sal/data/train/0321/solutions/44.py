class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        a1 = [s1[i] >= s2[i] for i in range(len(s1))]
        a2 = [s1[i] <= s2[i] for i in range(len(s1))]
        return False not in a1 or False not in a2
