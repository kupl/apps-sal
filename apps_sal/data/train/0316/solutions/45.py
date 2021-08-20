class Solution:

    def longestPrefix(self, s: str) -> str:
        lps = [0]
        for i in range(1, len(s)):
            pos = lps[-1]
            if s[pos] == s[i]:
                lps.append(1 + lps[-1])
            else:
                pos = lps[lps[-1] - 1]
                if s[pos] == s[i]:
                    lps.append(1 + pos)
                else:
                    lps.append(0)
        return s[:lps[-1]]
