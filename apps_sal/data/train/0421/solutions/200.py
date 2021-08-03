class Solution:
    def lastSubstring(self, s: str) -> str:
        m = max(s)
        ans = ''
        for i in range(len(s)):
            ans = max(ans, s[i:])
        return ans
