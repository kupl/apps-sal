class Solution:
    def maxUniqueSplit(self, ss: str) -> int:
        @lru_cache(None)
        def dfs(s, words):
            if not s: return 0
            res = 0
            words = set(words)
            for i in range(len(s)):
                if s[:i+1] not in words:
                    res = max(res, 1 + dfs(s[i+1:], tuple(words | set([s[:i+1]]))))
            return res
        return dfs(ss, ())

