class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen = {0: -1}
        ret = curr = 0

        for i, c in enumerate(s):
            curr ^= 1 << ('aeiou'.find(c) + 1) >> 1
            if curr not in seen:
                seen[curr] = i
            ret = max(ret, i - seen[curr])

        return ret
