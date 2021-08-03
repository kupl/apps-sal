class Solution:
    # def findTheLongestSubstring(self, s: str) -> int:
    # Represent the counts (odd or even) of vowels with a bitmask.
    # Precompute the prefix xor for the bitmask of vowels and then get the longest valid substring.
    #
    def findTheLongestSubstring(self, s):
        seen = {0: -1}
        res = cur = 0
        for i, c in enumerate(s):
            cur ^= 1 << ('aeiou'.find(c) + 1) >> 1
            seen.setdefault(cur, i)
            res = max(res, i - seen[cur])
        return res
