VOWELS = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen = {0: -1}  # -1 to represent everything before the first letter
        mask = 0
        longest = 0
        for ind, char in enumerate(s):
            mask ^= VOWELS.get(char, 0)  # Key is that mask will be 0 when all vowels are even
            if mask not in seen:
                seen[mask] = ind
            else:  # If we see same nonzero mask, seen[mask]+1 to ind (both inclusive) is even
                longest = max(longest, ind - seen[mask])
        return longest
