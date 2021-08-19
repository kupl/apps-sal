class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {x: 1 << i for (i, x) in enumerate('aeiou')}
        fst = {0: -1}
        ans = mask = 0
        for (i, c) in enumerate(s):
            if c in vowels:
                mask ^= vowels[c]
            fst.setdefault(mask, i)
            ans = max(ans, i - fst[mask])
        return ans
