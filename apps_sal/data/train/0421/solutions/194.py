class Solution:

    def lastSubstring(self, s: str) -> str:
        l = 0
        r = len(s)
        max_s = s
        while l < r:
            if s[l:r] >= max_s:
                max_s = s[l:r]
            l += 1
        return max_s
