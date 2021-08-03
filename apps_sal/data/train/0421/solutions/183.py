class Solution:
    def lastSubstring(self, s: str) -> str:

        maximum = s
        for i in range(1, len(s)):
            if s[i:] > maximum:
                maximum = s[i:]

        return maximum
