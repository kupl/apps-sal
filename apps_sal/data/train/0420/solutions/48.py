class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        vowels_bit_mask = {v: 2 ** i for (i, v) in enumerate('aeiou')}
        vowel_state = 0
        first_index_of_recorded_state = {0: -1}
        max_substr_len = 0
        for (index, char) in enumerate(s):
            if char in vowels_bit_mask:
                vowel_state ^= vowels_bit_mask[char]
            if vowel_state in first_index_of_recorded_state:
                max_substr_len = max(max_substr_len, index - first_index_of_recorded_state[vowel_state])
            else:
                first_index_of_recorded_state[vowel_state] = index
        return max_substr_len
