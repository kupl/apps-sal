class Solution:
    def lastSubstring(self, s: str) -> str:
        dicmap = {}
        maxhold = s[0]
        index = 0

        for i in range(0, len(s)):
            if s[i:] > maxhold:
                maxhold = s[i:]
                index = i

        return s[index:]
