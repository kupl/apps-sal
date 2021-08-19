class Solution:

    def longestPrefix(self, s: str) -> str:
        (j, prefix, suffix) = (0, 0, 0)
        mod = 10 ** 9 + 9
        for i in range(len(s) - 1):
            prefix = (prefix * 128 + ord(s[i])) % mod
            suffix = (suffix + pow(128, i, mod) * ord(s[-i - 1])) % mod
            if prefix == suffix:
                j = i + 1
        return s[:j]
