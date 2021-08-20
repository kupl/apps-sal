class Solution:

    def maxVowels(self, s, k):
        (vcnt, res) = (dict(), 0)
        for (i, c) in enumerate(s):
            if i - k >= 0 and s[i - k] in 'aeiou':
                vcnt[s[i - k]] -= 1
            if c in 'aeiou':
                vcnt[c] = vcnt.get(c, 0) + 1
            res = max(res, sum(vcnt.values()))
        return res


class Solution:

    def maxVowels(self, s, k):
        (res, cnt) = (0, 0)
        for (i, c) in enumerate(s):
            cnt += (c in 'aeiou') - (i - k >= 0 and s[i - k] in 'aeiou')
            if cnt > res:
                res = cnt
        return res
