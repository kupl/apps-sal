class Solution:
    def lastSubstring(self, s: str) -> str:
        largest_character = max(set(s))
        result = ''
        ind = [i for i, char in enumerate(s) if char == largest_character]

        # for i, char in enumerate(s):
        for i in ind:

            # if char==largest_character:
            result = max(result, s[i:])

        return result
