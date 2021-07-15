class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # prefix sum strategy with smart tricks for simplicity
        seen, vowel = {0: -1}, {'a':0,'e':1,'i':2,'o':3,'u':4}
        res = curr = 0
        for i, c in enumerate(s):
            # only update curr when it's a vowel
            if c in vowel:
                curr ^= 1 << vowel[c]
            # insert if not existing or update if exists
            seen.setdefault(curr, i)
            res = max(res, i - seen[curr])
        return res
