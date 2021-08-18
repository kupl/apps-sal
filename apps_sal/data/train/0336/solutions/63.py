class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps = 0
        myDict = {}

        for c in s:
            if c in myDict:
                myDict[c] += 1
            else:
                myDict[c] = 1

        for c in t:
            if c in myDict:
                myDict[c] -= 1
                if myDict[c] == 0:
                    del myDict[c]
            else:
                steps += 1

        return steps
