class Solution:
    def lastSubstring(self, s: str) -> str:
        max_a = max(s)
        sub = s
        for i in range(len(s)):
            if s[i] == max_a:
                if s[i:] > sub:
                    sub = s[i:]
        return sub

