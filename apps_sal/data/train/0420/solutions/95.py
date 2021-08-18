class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = 'aeiou'
        mask = last_mask = 0
        first = [-1] + [float('inf')] * 31
        last = [-1] + [float('-inf')] * 31
        for i, c in enumerate(s):
            if c in set(vowels):
                j = vowels.index(c)
                last_mask, mask = mask, mask ^ (1 << j)
                if first[mask] == float('inf'):
                    first[mask] = last[last_mask] + 1
            last[mask] = i
        return max(j - i for i, j in zip(first, last) if j - i <= len(s))
