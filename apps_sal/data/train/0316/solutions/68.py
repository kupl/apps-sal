class Solution:

    def longestPrefix(self, s: str) -> str:
        n = len(s)
        k = n - 1
        while k > 0:
            if s[:k] == s[-k:]:
                break
            k -= 1
        return s[:k]
