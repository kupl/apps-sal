class Solution:

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ar1 = [0 for i in range(len(s1))]
        ar2 = [0 for i in range(len(s2))]
        for i in range(len(s1)):
            ar1[i] = ord(s1[i])
            ar2[i] = ord(s2[i])
        ar1.sort()
        ar2.sort()
        flag1 = False
        flag2 = False
        for i in range(len(ar1)):
            if ar1[i] - ar2[i] < 0:
                flag1 = True
            elif ar2[i] - ar1[i] < 0:
                flag2 = True
        return flag1 == False or flag2 == False
