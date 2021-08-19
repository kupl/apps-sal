class Solution:

    def lastSubstring(self, s: str) -> str:
        ans = ''
        c = max(s)
        idx = [i for i in range(len(s)) if s[i] == c]
        for i in idx:
            ans = max(ans, s[i:])
        return ans
