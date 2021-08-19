class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        count1 = 0
        count2 = 0
        for i in range(len(s1)):
            if s1[i] <= s2[i]:
                count1 += 1
            if s1[i] >= s2[i]:
                count2 += 1
        if count1 == len(s1) or count2 == len(s1):
            return True
        return False
