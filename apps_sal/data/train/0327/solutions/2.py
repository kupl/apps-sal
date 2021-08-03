class Solution:
    def lengthOfLongestSubstring(self, s):
        char_dict = {}
        longest_run = 0
        current_run = 0
        distance = 2

        for i, char in enumerate(s):
            if char in char_dict:
                distance = i - char_dict[char]
                if distance <= current_run:
                    current_run = distance
                else:
                    current_run += 1
            else:
                current_run += 1

            char_dict[char] = i
            if current_run > longest_run:
                longest_run = current_run
        return longest_run
