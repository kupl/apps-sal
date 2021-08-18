class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
        seen = {0: -1}
        res = cur = 0
        for i, c in enumerate(s):
            if c in vowels:
                cur ^= 1 << vowels[c]
                seen.setdefault(cur, i)
            res = max(res, i - seen[cur])
        return res
