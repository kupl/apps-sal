class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        count1 = 0
        count2 = 0
        for i in range(len(s1)):
            count1 += 1 * (s1[i] >= s2[i])
            count2 += 1 * (s1[i] <= s2[i])
        return count1 == len(s1) or count2 == len(s1)
