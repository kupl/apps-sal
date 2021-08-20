class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = 0
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        max_vowels = vowel_count
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                vowel_count -= 1
            if s[i] in vowels:
                vowel_count += 1
            max_vowels = vowel_count if vowel_count > max_vowels else max_vowels
        return max_vowels
