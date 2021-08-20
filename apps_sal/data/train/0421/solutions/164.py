class Solution:

    def lastSubstring(self, s: str) -> str:
        c = max(s)
        maxSub = ''
        loc = s.find(c, 0)
        while loc != -1:
            maxSub = max(maxSub, s[loc:])
            loc = s.find(c, loc + 1)
        return maxSub
