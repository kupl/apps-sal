class Solution:
    def longestPrefix(self, s: str) -> str:
        # KMP
        lps = [0] * len(s)
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[j] != s[i]:
                j = lps[j - 1]
            if s[j] == s[i]:
                lps[i] = j + 1
                j += 1
        return s[:lps[-1]]
