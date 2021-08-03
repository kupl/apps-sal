class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited = set()

        def dfs(start):
            nonlocal visited
            if start == len(s):
                return 0
            res = 0
            for i in range(start, len(s)):
                if s[start:i + 1] not in visited:
                    visited.add(s[start:i + 1])
                    res = max(res, 1 + dfs(i + 1))
                    visited.remove(s[start:i + 1])
                else:
                    res = max(res, dfs(i + 1))
            return res
        return dfs(0)
