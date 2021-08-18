
class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        def is_a_vowel(letter): return letter in 'aeiou'

        count = 0
        maximum_vowels = 0

        left = 0

        for right in range(len(s)):
            if right < k:
                count = count + 1 if is_a_vowel(s[right]) else count
                maximum_vowels = max(maximum_vowels, count)
            else:
                count = max(0, count - 1) if is_a_vowel(s[left]) else count
                count = count + 1 if is_a_vowel(s[right]) else count
                left = left + 1
                maximum_vowels = max(maximum_vowels, count)

        return maximum_vowels
