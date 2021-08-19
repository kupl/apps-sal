class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        seen = set()

        def dfs(s, seen=seen):
            if not s:
                return 0
            res = 0
            for i in range(1, len(s) + 1):
                if s[:i] in seen:
                    continue
                seen.add(s[:i])
                res = max(res, 1 + dfs(s[i:]))
                seen.remove(s[:i])
            return res
        return dfs(s)
