class Solution:

    def func(self, s, idx, words):
        max_result = 0
        for i in range(idx + 1, len(s)):
            max_result = max(max_result, self.func(s, i, words | {s[idx:i]}))
        max_result = max(max_result, len(words | {s[idx:]}))
        return max_result

    def maxUniqueSplit(self, s: str) -> int:
        return self.func(s, 0, set())
