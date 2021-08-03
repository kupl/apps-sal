class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        self.res = 0

        def dfs(strs, s):
            if not s:
                if len(set(strs)) == len(strs):
                    self.res = max(self.res, len(strs))
                return
            dfs(strs + [s[0]], s[1:])

            if strs:
                dfs(strs[:-1] + [strs[-1] + s[:1]], s[1:])

            return

        dfs([], s)

        return self.res
