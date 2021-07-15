class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Sliding window with fixed width (=k)
        vowels = 'aeiou'
        num_vowels = sum(1 for i in range(k) if s[i] in vowels)
        max_vowels = num_vowels
        for removed_idx in range(0, len(s) - k):
            added_idx = removed_idx + k
            num_vowels += int(s[added_idx] in vowels) - int(s[removed_idx] in vowels)
            if num_vowels > max_vowels:
                max_vowels = num_vowels
        return max_vowels
