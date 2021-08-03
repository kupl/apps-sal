class Solution:
    def lastSubstring(self, s: str) -> str:

        max_letter = max(s)

        curr_max_index = s.find(max_letter)
        curr_substring = s[curr_max_index:]

        output = s

        next_max_index = 0

        while (True):
            next_max_index = s.find(max_letter, curr_max_index + 1)
            if next_max_index == -1:
                return max(curr_substring, output)

            if curr_substring > output:
                output = curr_substring

            curr_max_index = next_max_index
            curr_substring = s[curr_max_index:]

            if output > curr_substring:
                continue
