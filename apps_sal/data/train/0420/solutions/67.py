class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # bitmask aeiou with xxxxx
        mask, seen, smax, vowels = 0, {0: -1}, 0, {x: 1 << i for i, x in enumerate('aeiou')}
        for i, x in enumerate(s):
            if x in vowels:
                mask ^= 1 << vowels[x]
            seen.setdefault(mask, i)
            smax = max(smax, i - seen[mask])
        return smax
