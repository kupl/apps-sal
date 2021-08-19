class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        aeiou = {c: i for (i, c) in enumerate('aeiou')}
        seen = {0: -1}
        res = curr = 0
        for (i, c) in enumerate(s):
            curr ^= 1 << aeiou.get(c, -1) + 1 >> 1
            seen.setdefault(curr, i)
            res = max(res, i - seen[curr])
        return res
