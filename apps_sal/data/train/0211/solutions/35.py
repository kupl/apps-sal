
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        if not s:
            return 0
        return self.dfs(s, set())

    def dfs(self, s: str, present: set) -> int:
        maximum = 0

        for i in range(1, len(s) + 1):
            substring = s[:i]
            if substring not in present:
                sub_try = self.dfs(s[i:], {*present, substring})
                maximum = max(maximum, 1 + sub_try)
        return maximum
