class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        seen = {0: -1}
        pos = {c: i for (i, c) in enumerate('aeiou')}
        curr = res = 0
        for (i, c) in enumerate(s):
            curr ^= 1 << pos.get(c, -1) + 1 >> 1
            seen.setdefault(curr, i)
            res = max(res, i - seen[curr])
        return res
