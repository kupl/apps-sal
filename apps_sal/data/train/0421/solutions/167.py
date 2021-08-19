class Solution:

    def lastSubstring(self, s: str) -> str:
        input_string = s
        max_letter = max(input_string)
        curr_max_index = input_string.find(max_letter)
        curr_substring = input_string[curr_max_index:]
        output = input_string
        next_max_index = 0
        while True:
            next_max_index = input_string.find(max_letter, curr_max_index + 1)
            if next_max_index == -1:
                return max(curr_substring, output)
            if curr_substring > output:
                output = curr_substring
            curr_max_index = next_max_index
            curr_substring = input_string[curr_max_index:]
            if output > curr_substring:
                continue
