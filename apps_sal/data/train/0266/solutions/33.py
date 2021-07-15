class Solution:
    def numSplits(self, s: str) -> int:
        
        auxDict = {}
        auxLeftToRight = [0] * len(s)
        count = 0
        for pos in range(len(s)):
            if s[pos] not in auxDict:
                auxDict[s[pos]] = 1
                count += 1
            auxLeftToRight[pos] = count

        auxDict = {}
        auxRightToLeft = [0] * len(s)
        count = 0
        for pos in range(len(s)-1):
            if s[len(s)-1-pos] not in auxDict:
                auxDict[s[len(s)-1-pos]] = 1
                count += 1
            auxRightToLeft[len(s)-2-pos] = count

        total = 0
        for pos in range(len(s)):
            if auxLeftToRight[pos] == auxRightToLeft[pos]:
                total += 1
        
        return total

