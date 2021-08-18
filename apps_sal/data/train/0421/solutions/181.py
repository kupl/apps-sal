class Solution:
    def lastSubstring(self, s: str) -> str:
        largest_character = max(set(s))
        result = ''
        ind = [i for i, char in enumerate(s) if char == largest_character]

        for i in ind:

            result = max(result, s[i:])

        return result
