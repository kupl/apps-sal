VOWELS = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}


class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        seen = {0: -1}
        mask = 0
        longest = 0
        for (ind, char) in enumerate(s):
            mask ^= VOWELS.get(char, 0)
            if mask not in seen:
                seen[mask] = ind
            else:
                longest = max(longest, ind - seen[mask])
        return longest
