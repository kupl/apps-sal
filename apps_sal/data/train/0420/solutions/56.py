class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen, vowel = {0: -1}, {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        res = curr = 0
        for i, c in enumerate(s):
            if c in vowel:
                curr ^= 1 << vowel[c]
            seen.setdefault(curr, i)
            res = max(res, i - seen[curr])
        return res
