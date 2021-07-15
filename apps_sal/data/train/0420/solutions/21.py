from copy import copy

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel2idx = dict([(item[1], item[0]) for item in enumerate(['a', 'e', 'i', 'o', 'u'])])
        
        counters = [0]
        for item in s:
            counters.append(counters[-1])
            if item in vowel2idx:
                counters[-1] ^= (2 ** vowel2idx[item])
        
        for width in range(len(s), 0, -1):
            for start in range(len(s) - width + 1):
                if counters[start + width] ^ counters[start] != 0:
                    continue
                return width
        return 0

