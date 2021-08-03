

class Solution:

    def lastSubstring(self, s: str) -> str:

        start_char = 'a'
        ans = 'a'

        for i in range(len(s)):

            if s[i] > start_char:
                start_char = s[i]
                ans = s[i:]

        for i in range(len(s)):

            if s[i] == start_char:
                ans = max(ans, s[i:])

        return ans
