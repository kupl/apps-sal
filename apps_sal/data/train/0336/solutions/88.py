class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countChars = dict()
        for i in s:
            if i in countChars:
                countChars[i][0] += 1
            else:
                countChars[i] = [1,0]
        
        ctr = 0
        
        for j in t:
            if j in countChars:
                countChars[j][1] += 1
            else:
                countChars[j] = [0,1]
                
        for i in countChars:
            if countChars[i][0] > countChars[i][1]:
                ctr += countChars[i][0] - countChars[i][1]
        return ctr
