class Solution:

    def lastSubstring(self, s: str) -> str:
        max = s
        for i in range(len(s)):
            if max < s[i:]:
                max = s[i:]
        return max
