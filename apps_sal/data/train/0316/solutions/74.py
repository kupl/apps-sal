class Solution:

    def longestPrefix(self, s: str) -> str:
        (res, l, r, mod) = (0, 0, 0, 10 ** 9 + 7)
        for i in range(len(s) - 1):
            l = (l * 128 + ord(s[i])) % mod
            r = (ord(s[~i]) * pow(128, i, mod) + r) % mod
            if l == r:
                res = i + 1
        return s[:res]

    def longestPrefix_bychance_Brute(self, s: str) -> str:
        res = ''
        for i in range(1, len(s)):
            if s[:i] == s[-i:]:
                res = s[:i]
        return res
