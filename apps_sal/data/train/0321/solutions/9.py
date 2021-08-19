class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        s1token = True
        for i in range(len(s1)):
            if s1[i] > s2[i]:
                s1token = False
                break
        if s1token == True:
            return True
        s2token = True
        for i in range(len(s2)):
            if s2[i] > s1[i]:
                s2token = False
                break
        if s2token == True:
            return True
        return False
