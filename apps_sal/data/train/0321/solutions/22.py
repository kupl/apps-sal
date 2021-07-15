class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1, reverse=True)
        s2 = sorted(s2, reverse=True)

        resultA = []
        resultB = []
        
        for ch1, ch2 in zip(s1, s2):
            if ch1 >= ch2:
                resultA.append(1)
            else:
                resultA.append(0)
                
            if ch2 >= ch1:
                resultB.append(1)
            else:
                resultB.append(0)
        
        if all(resultA) == 1 or all(resultB):
            return True
        else:
            return False
