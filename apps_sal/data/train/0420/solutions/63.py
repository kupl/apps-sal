class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        (n, vowels, d) = (len(s), 'aeiou', {0: -1})
        ret = cur = 0
        for (i, c) in enumerate(s):
            if c in vowels:
                cur ^= 1 << vowels.index(c)
            d.setdefault(cur, i)
            ret = max(ret, i - d[cur])
        return ret
