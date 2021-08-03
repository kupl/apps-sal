class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res = cur = 0
        seen = {0: -1}
        for i, c in enumerate(s):
            cur ^= 1 << ('aeiou'.find(c) + 1) >> 1
            seen.setdefault(cur, i)
            res = max(res, i - seen.get(cur))
        return res
