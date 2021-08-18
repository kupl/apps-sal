

class Solution:

    def lastSubstring(self, s: str) -> str:

        start_char = max(s)
        ans = start_char

        for i in range(len(s)):
            if s[i] == start_char:
                ans = max(ans, s[i:])

        return ans
