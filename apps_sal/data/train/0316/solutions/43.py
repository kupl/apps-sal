class Solution:

    def longestPrefix(self, s: str) -> str:
        par = [0] * len(s)
        for i in range(1, len(s)):
            j = par[i - 1]
            while j and s[j] != s[i]:
                j = par[j - 1]
            j += int(s[i] == s[j])
            par[i] = j
        return s[:par[-1]]
