class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        lenS = len(s)

        uniqSubStrDict = {}

        count = 0

        Max = 0
        for i in range(minSize, maxSize + 1):
            for j in range(lenS - i + 1):

                tstSubStr = s[j: j + i]
                uniqChars = {}
                for k in tstSubStr:
                    uniqChars[k] = 1

                if len(uniqChars) > maxLetters:
                    continue

                uniqSubStrDict[tstSubStr] = uniqSubStrDict.get(tstSubStr, 0) + 1

                if uniqSubStrDict[tstSubStr] > Max:
                    Max = uniqSubStrDict[tstSubStr]

        count = Max

        return count
