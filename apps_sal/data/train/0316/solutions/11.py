class Solution:

    def longestPrefix(self, s: str) -> str:
        ls = len(s)
        id = -1
        for i in range(ls - 1):
            if s[0:i + 1] == s[ls - i - 1:ls]:
                id = i
        return s[:id + 1]
