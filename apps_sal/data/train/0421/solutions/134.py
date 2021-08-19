class Solution:

    def lastSubstring(self, s: str) -> str:
        max_letter = max(s)
        curr_max_index = s.find(max_letter)
        curr_substring = s[curr_max_index:]
        output = s
        next_max_index = 0
        while next_max_index != -1:
            next_max_index = s.find(max_letter, curr_max_index + 1)
            if curr_substring > output:
                output = curr_substring
            curr_max_index = next_max_index
            curr_substring = s[curr_max_index:]
        return output
