class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.res = 0

        def dfs(s, path):
            if not s:
                self.res = max(self.res, len(path))
            for i in range(1, len(s) + 1):
                dfs(s[i:], path | {s[:i]})
        dfs(s, set())
        return self.res
