class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        
        ge = 0
        le = 0
        for i in range(len(s1)):
            if s1[i] >= s2[i]:
                ge += 1
            if s1[i] <= s2[i]:
                le += 1

        return ge == len(s1) or le == len(s1)

