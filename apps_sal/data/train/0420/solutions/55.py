class Solution:
    # \"Time: O(n), Space: O(number of unique vowel count sequences)\"
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        # \"d: last_seen_index_for_vowel_sequence_count_map\"
        d, bit_represenation_for_vowel_count, result = {0: -1}, 0, 0
        for i, c in enumerate(s):
            if c in vowels:
                # \"n would be 0 if count is even\"
                bit_represenation_for_vowel_count ^= vowels[c]
            # \"any combination of vowels that gives odd count & have not been seen before\"
            if bit_represenation_for_vowel_count not in d:  
                # \"stores the oldest index for which a particular combination of vowels resulted into odd count\"
                d[bit_represenation_for_vowel_count] = i
            else:
                # \"if a combination is seen again, result = current_index - last_seen_index_for_this_combination (d[n])\"
                # \"example: s = \"aepqraeae\" (odd vowel count for s[:2] is seen again at s[0:]\"
                # \"not considering character at last seen index will make count even\"
                result = max(result, i - d[bit_represenation_for_vowel_count])
        return result
