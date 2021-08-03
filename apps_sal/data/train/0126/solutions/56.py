class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        maxOcc = 0
        strOcc = {}

        for i in range(minSize, maxSize + 1):
            charFreq = {}
            sub = s[:i]
            uniqueChar = 0

            for c in sub:
                if c not in charFreq:
                    charFreq[c] = 0
                    uniqueChar += 1
                charFreq[c] += 1

            if uniqueChar <= maxLetters:
                if sub not in strOcc:
                    strOcc[sub] = 0
                strOcc[sub] += 1
                maxOcc = max(maxOcc, strOcc[sub])

            for j in range(i, len(s)):
                outC = sub[0]
                inC = s[j]

                charFreq[outC] -= 1
                if charFreq[outC] == 0:
                    uniqueChar -= 1
                    del charFreq[outC]

                if inC not in charFreq:
                    charFreq[inC] = 0
                    uniqueChar += 1
                charFreq[inC] += 1

                sub = sub[1:] + inC

                if uniqueChar <= maxLetters:
                    if sub not in strOcc:
                        strOcc[sub] = 0
                    strOcc[sub] += 1
                    maxOcc = max(maxOcc, strOcc[sub])

        return maxOcc
