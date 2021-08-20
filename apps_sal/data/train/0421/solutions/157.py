class Solution:

    def lastSubstring(self, s: str) -> str:
        bestStr = s
        bestChar = s[0]
        for i in range(1, len(s)):
            if s[i] >= bestChar and s[i:] > bestStr:
                bestChar = s[i]
                bestStr = s[i:]
        return bestStr
