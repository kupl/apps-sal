class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        LPS = [0] * n

        i = 1
        longestprefix = 0
        while i < n:
            if s[longestprefix] == s[i]:
                longestprefix += 1
                LPS[i] = longestprefix
                i += 1
            else:
                if longestprefix > 0:
                    longestprefix = LPS[longestprefix - 1]
                else:
                    i += 1
        return s[:LPS[-1]]
