class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        if not s or not k:
            return 0
        max_vowels = 0
        start_pointer = 0
        end_pointer = k - 1
        vowels = {'a', 'e', 'i', 'o', 'u'}
        num_curr_window_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                num_curr_window_vowels += 1
        max_vowels = max(max_vowels, num_curr_window_vowels)
        while end_pointer < len(s) - 1:
            if s[start_pointer] in vowels:
                num_curr_window_vowels -= 1
            start_pointer += 1
            end_pointer += 1
            if s[end_pointer] in vowels:
                num_curr_window_vowels += 1
            max_vowels = max(max_vowels, num_curr_window_vowels)
        return max_vowels
