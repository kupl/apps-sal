class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = sorted(s1)
        s2 = sorted(s2)
        s1_tally = 0
        s2_tally = 0
        for i in range(n):
            if s1[i] >= s2[i]:
                s1_tally += 1
            if s2[i] >= s1[i]:
                s2_tally += 1
        return s1_tally == n or s2_tally == n
