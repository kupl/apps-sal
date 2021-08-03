class Solution:
    def lastSubstring(self, s: str) -> str:

        length = len(s)

        maxChar = ''
        maxCharIdxs = []

        for i in range(length):
            maxChar = max(s[i], maxChar)

        for idx, char in enumerate(s):
            if char == maxChar:
                maxCharIdxs.append(idx)

        maxSubstr = ''
        for maxIdx in maxCharIdxs:
            maxSubstr = max(s[maxIdx:], maxSubstr)

        return maxSubstr
