class Solution:

    def lastSubstring(self, s: str) -> str:
        if not s:
            return ''
        if len(set(s)) == 1:
            return s
        largest = max(list(s))
        currmax = ''
        for (i, c) in enumerate(s):
            if c == largest:
                if s[i:] > currmax:
                    currmax = s[i:]
        return currmax
