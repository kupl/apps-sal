class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        helper_dict = {}
        longest_start = 0
        longest_end = -1
        current_start = 0
        for (char_index, char) in enumerate(s):
            if char not in helper_dict or helper_dict[char] < current_start:
                helper_dict[char] = char_index
            else:
                current_start = helper_dict[char] + 1
                helper_dict[char] = char_index
            if char_index - current_start > longest_end - longest_start:
                longest_start = current_start
                longest_end = char_index
        return longest_end - longest_start + 1
