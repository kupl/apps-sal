class Solution:
    def longestPrefix(self, s: str) -> str:
        l = len(s)
        nx = [-1] * (l + 1)
        i, j = 0, -1
        while i < l:
            while j == -1 or (i < l and s[i] == s[j]): 
                i += 1
                j += 1
                nx[i] = j
            if i < l and s[i] != s[j]: j = nx[j]
        return s[:nx[-1]]
