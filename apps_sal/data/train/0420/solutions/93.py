from copy import copy


class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        vowel2idx = dict([(item[1], item[0]) for item in enumerate(['a', 'e', 'i', 'o', 'u'])])
        counters = [[0] * len(vowel2idx)]
        for item in s:
            counters.append(counters[-1].copy())
            if item in vowel2idx:
                counters[-1][vowel2idx[item]] += 1
        for width in range(len(s), 0, -1):
            for start in range(len(s) - width + 1):
                for n_vowels in map(int.__sub__, counters[start + width], counters[start]):
                    if n_vowels % 2 == 1:
                        break
                else:
                    return width
        return 0
