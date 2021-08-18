class Solution:
    def lastSubstring(self, s: str) -> str:
        ans = s[0]
        for i in range(len(s)):
            if s[i] < ans[0]:
                continue
            else:

                ans = max(s[i:], ans)
        return ans
