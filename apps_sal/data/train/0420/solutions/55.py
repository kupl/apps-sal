class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        (d, bit_represenation_for_vowel_count, result) = ({0: -1}, 0, 0)
        for (i, c) in enumerate(s):
            if c in vowels:
                bit_represenation_for_vowel_count ^= vowels[c]
            if bit_represenation_for_vowel_count not in d:
                d[bit_represenation_for_vowel_count] = i
            else:
                result = max(result, i - d[bit_represenation_for_vowel_count])
        return result
