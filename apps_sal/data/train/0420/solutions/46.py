class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        bits = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        d = {0: -1}
        n = 0
        res = 0
        for (i, c) in enumerate(s):
            if c in bits:
                n ^= bits[c]
            if n not in d:
                d[n] = i
            else:
                res = max(res, i - d[n])
        return res
