class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res = 0

        cur = 0
        seen = {0: -1}
        for i, char in enumerate(s):
            cur ^= 1 << ('aeiou'.find(char) + 1) >> 1
            if cur not in seen:
                seen[cur] = i
            res = max(res, i - seen[cur])

        return res
