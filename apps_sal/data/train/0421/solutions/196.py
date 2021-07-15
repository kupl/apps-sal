class Solution:
    def lastSubstring(self, s: str) -> str:
        ans = s
        for i in range(1, len(s)):
            ans = max(ans, s[i:])
        return ans
