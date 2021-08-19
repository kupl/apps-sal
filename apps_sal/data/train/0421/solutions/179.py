class Solution:

    def lastSubstring(self, s: str) -> str:
        mx = max(s)
        pos = [i for i in range(len(s)) if s[i] == mx]
        return max((s[i:] for i in pos))
