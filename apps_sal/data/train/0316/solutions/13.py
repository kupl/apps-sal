class Solution:

    def longestPrefix(self, s: str) -> str:
        max_index = -1
        for (index, _) in enumerate(s[:-1]):
            if s[:index + 1] == s[-1 * (index + 1):]:
                max_index = index
        return s[:max_index + 1]
