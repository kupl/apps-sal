class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        s1_bigger = False
        s2_bigger = False
        for i in range(len(s1)):
            if s1_bigger and s1[i] < s2[i]:
                return False
            if s2_bigger and s1[i] > s2[i]:
                return False
            if s1[i] < s2[i]:
                s2_bigger = True
            if s1[i] > s2[i]:
                s1_bigger = True
        return True
