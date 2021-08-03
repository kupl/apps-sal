class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(s, path):
            res = 0
            if not s:
                return len(path)
            for i in range(1, len(s) + 1):
                res = max(res, dfs(s[i:], path | {s[:i]}))
            return res
        return dfs(s, set())
