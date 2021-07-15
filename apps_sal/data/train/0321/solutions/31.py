class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted([ord(s) for s in s1])
        s2 = sorted([ord(s) for s in s2])
        i = 0 
        while s1[i] <= s2[i]:
            if i == len(s1) - 1: 
                return True
            i += 1
        i = 0
        while s2[i] <= s1[i]:
            if i == len(s1) - 1: 
                return True
            i += 1
        return False 
