class Solution:
    def maxVowels(self, s, k):
        vcnt, res = dict(), 0
        for i, c in enumerate(s):
            if i - k >= 0 and s[i - k] in 'aeiou':
                vcnt[s[i - k]] -= 1
            if c in 'aeiou':
                vcnt[c] = vcnt.get(c, 0) + 1
            res = max(res, sum(vcnt.values()))
        return res
