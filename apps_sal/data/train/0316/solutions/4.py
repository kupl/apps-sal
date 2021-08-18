class Solution:
    def longestPrefix(self, s):
        num_chars = 26
        res, l, r, mod = 0, 0, 0, 10**9 + 7

        for i in range(len(s) - 1):

            l = (l * num_chars + ord(s[i])) % mod

            r = (r + pow(num_chars, i, mod) * ord(s[~i])) % mod

            if l == r:
                res = i + 1

        return s[:res]
